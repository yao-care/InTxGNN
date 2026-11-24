# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）。
本站照 UsTxGNN 的試做版建立，規則與程式都在本 repo，頁面文字用英文、依據是印度藥品資料集（junioralive/Indian-Medicine-Dataset，站上原本的來源）。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁「## Review Log」表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/intxgnn/regulatory/page_format.py` | 頁首＝Quick Overview「Evidence Level」格的**第一個**等級（主預測）。2026-11-12 實測本站現有頁面全部是這個規則（第一個等級跟格內最高等級不同的頁也照第一個），照實寫成程式；Tw 是整格取最高，本站不同 |
| 撤回預測 | `src/intxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/in_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/intxgnn/regulatory/licenses.py` | 快照存事實層與本藥號碼；gate 依快照驗市場段落的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包的許可證紀錄目前沒有適應症文字時，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 許可證修正時直接刪掉的矛盾子句（10-31 dcc29335e、11-06 a373ef9df（單方／複方說法）），2026-11-12 由 scripts/reviews_from_edits.py 依 git 前後版本轉入。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。
2026-11-12：sodium_feredetate 的 11-06 刪句（a373ef9df）在「no|ne」中間切斷，留下「One has been cancelled.」（意思相反，資料 6 筆都沒有停產）；重發 `in-lic-20261106-sodium_feredetate-1`，改成只刪單方子句、保留「None has been cancelled.」，前版存在 history。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 817 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Currently, detailed mechanism of action data is not available in the data compiled for this report.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `in-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：「According to the … section of the US FDA-approved prescribing information for <藥>: "…" ([DailyMed: …](…), label version …; accessed …)」。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 2026-11-19 結果：657 頁寫入紀錄（美國仿單 566、ChEMBL 91），160 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 10 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）37 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Approved use: Not recorded in the local data」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：第三方整理的價格資料集（not discontinued）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abacavir「Approved use: Not recorded in the local data」→「In India: 9 listed products (9 not discontinued)」；2026-11-19 改了 417 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site InTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 市場段落品項表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站「許可證張數與狀態不再每週過期」，本站做表＋B）：每週排程只改得到概覽表狀態列／張數列，市場段落 AI 寫的自由格式表（表頭多是「Authorization Number | Product Name | Dosage Form | Approved Indication」，後者全是 Not recorded）與正文寫死的張數會跟每週變的資料集矛盾。本站資料是第三方整理的印度藥品價格資料集（Indian Medicine Dataset，Is_discontinued），不是 CDSCO 許可證，表與句子照這個口徑寫。
- A. `scripts/sync_license_tables.py`：「## India Market Information」的第一張許可證表換成程式依證據包產生的表「| Dataset ID | Product Name | Pack Size | Status |」（品名、包裝照資料集原文；狀態 Valid／Discontinued；未停產在前、依 ID 數字排序；證據包全部紀錄，最多 20 筆），表下來源句（不寫狀態字），部分紀錄的頁加既有的「Only part of the licence list is held in the data; the list may be incomplete.」；段落沒有表時放段落開頭，沒有段落的頁（5 頁）不加。
  不放成分欄（證據包 ingredients 只收了 short_composition1，複方第二成分沒收）、不放廠商欄（itraconazole「GRAF Laboratories」會被 checker P5 當成知識圖譜字樣）。
  前後 `<!-- licenses:begin/end -->`；快照 `snapshots/in_licenses.json.gz` 存 rows／show（program_rows），gate 第 18 項（`src/intxgnn/regulatory/licenses.py`）擋「程式區塊≠快照重算」「市場段落沒有程式區塊」。
  接進：`scripts/apply_drug_reviews.py`（非 --check）結尾、`scripts/build_license_snapshot.py` 結尾（不給 --ws 時只跑表與 B）、`scripts/license_adapter.py` 的 `sync_tables`（每週排程，--bundles）與 `PAGE_NOTE`（3b 放行程式區塊的非表格行）。
- B. `scripts/rewrite_license_counts.py`＋`src/intxgnn/regulatory/count_prose.py`（照 CaTxGNN 英文版移植，口徑改成本站：licence／registration／authorization／listing／product＋India／valid／dataset）：依快照事實層改寫句型明確的張數；有保留、講查詢、相對數、劑型或廠商子集、顯示筆數、partial 頁（517 個證據包中 439 頁）不動，單方張數不改（列 single），單複數、0 張、前提句列待查。gate 第 22 項擋「再跑一次會變」。事實層的單方數依資料集 short_composition2 判斷，2026-11-24 對 data/raw 原始 CSV 驗過非 partial 的 464 頁全部一致。
- 2026-11-24 第一次套用（Release data-20261112-161012）：898 頁換成程式表（公開頁 881、noindex 17；原有表 891 頁、段落裡沒有許可證表的 7 頁補在段落開頭）；`--migrate` 拿掉只講舊表筆數的說明句 428 處與舊的部分紀錄提示行 15 行；改頁的 last_modified_at 改 2026-11-24。
  B 改寫 0 句（現行事實全部有效、張數句跟事實一致；判斷不了 0 句）。錨在舊表上的查核紀錄 0 筆（不用 superseded）。
  查核紀錄：53 筆 `in-lic-20261106-*` 更正文字裡寫死的張數與舊表筆數拿掉、同 id 重發（前版存 history；potassium_iodide 前版「All are are」一併修正）；說明（note）寫死「The data list N product records」的 6 筆改成不寫數字，`scripts/reviews_from_edits.py` 的 figures 樣板同改；
  另寫的寬偵測（單方說法對照 data/raw 原始資料集）找到 41 句說「全部單方／沒有複方」而證據包紀錄其實有複方，36 句以 `in-lic-20261124-*-1` 只刪單方字樣更正，5 句講「資料把它們歸為單方」列待查；
  正文仍講舊表列了哪幾筆（「A sixth licence … is also valid」「… are not shown」等）42 句列待查（source：市場段落換成程式許可證表後…）。checker 全量前後都是 0；gate exit 0。
- 母目錄 `.claude/license_labels/InTxGNN.json` 只有「Valid」：資料集標停產時程式表會寫「Discontinued」（目前 0 筆），要加 `"Discontinued": "cancelled"`（這次沒改母目錄）。

## 待查清單第二輪：舊表說法與單方說法逐句更正（2026-11-24）

用戶 2026-11-24 第二輪決定（第一輪列進待查的舊錯句逐句寫紀錄）。本站資料是第三方整理的印度藥品價格資料集（Indian Medicine Dataset），不是 CDSCO 許可證，更正文字照這個口徑、不寫死張數（指向概覽表與程式表）。
- 第一輪列待查的 47 句：42 句講舊 AI 表（「A sixth licence … is also valid」「… are not shown」「Three more are not shown above」「the table lists five examples」），換成全量程式表後相對說法不成立；5 句「資料把它們歸為單方」（doxofylline、metoclopramide、naproxen、pioglitazone、rosuvastatin），資料集 short_composition2 其實有第二成分。
  45 句以 `in-lic-20261124b-<藥>-1` 改寫（拿掉相對說法與寫死的張數，句中仍成立的品名、劑型、狀態照證據包保留；同句的單方說法跟資料集不符的 benzocaine、chlorzoxazone、ranitidine 一併改；fluphenazine、mupirocin、paliperidone、polyethylene_glycol 的劑型列舉照證據包全部紀錄改寫）；
  amylmetacresol、dexketoprofen、indacaterol、potassium_iodide 只刪舊表那句（replacement 空、anchor 指向前版紀錄的更正文字），esomeprazole 的 `in-lic-20261124-esomeprazole-1` 同 id 重發（更正文字的「All 20」在部分收錄頁不成立，前版存 history）。
  bacitracin（眼用 1、其餘軟膏或粉劑）、dapsone（口服 1、其餘 6 張凝膠）查證成立，標 resolved、不改頁。
- 同日另寫的寬偵測：單方說法 7 句（arginine、benzoic_acid、captopril、carisoprodol、daclatasvir、diosmin、nicergoline，非部分收錄頁的概述句，第一輪偵測沒涵蓋）只刪「single-ingredient」字樣；「classified as single-ingredient in the records」2 句（chlorzoxazone-2、pregabalin）照上面 5 句的做法；舊表說明句 4 句（pitavastatin「table below shows only … single-ingredient」、aripiprazole、etodolac、ofloxacin「Five main/representative … shown below」）刪掉。diatrizoate（meglumine＋sodium diatrizoate，同一成分的兩種鹽）不算複方，不改。
- 部分收錄頁（證據包存 20 筆、資料集更多）寫「20 valid single-ingredient registrations」之類、而存下的 20 筆有複方的 147 句列進待查（source：部分收錄頁的單方說法跟證據包已存紀錄不符）：資料集全量的單方品項數沒有逐藥核對，「at least 20 single-ingredient」可能成立，要人決定是否照 2026-11-06 做法一律刪字樣。
- calcitriol 證據包有 Calcirol 600000IU Injection（36119）：資料集原始檔把 cholecalciferol 產品的成分寫成「Calcitriol (600000IU)」（資料集另有 Devita、Osta D3 300000IU／600000IU Injection 同樣錯植，沒存進證據包），程式表照資料集原文；收錄規則沒改，列在上述待查項目的說明。
- `scripts/apply_drug_reviews.py` 的查核紀錄表說明句原本寫「checked against official Indian medicine data」，改成「the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices)」（129 頁的說明句）。
- 劑型全稱說法（only／all＋劑型）全量掃公開頁 408 句、依證據包劑型分類比對，標出的 14 句逐句讀過都成立，0 筆更正。市場段落沒有程式表的公開頁 3 頁（chlorpheniramine、docusate、ranolazine）是整頁沒有市場段落，照第一輪規則不加。
- 驗證：apply --check 0、rewrite_license_counts --check 0、checker 全量前後 0、gate exit 0。

## 第三輪：calcitriol 錯植品項排除、缺市場段落補段、部分收錄頁單方字樣（2026-11-24）

用戶 2026-11-24 第三輪決定。
- A. 證據包成分對照修正：資料集原始檔把 4 個 cholecalciferol（維生素 D3）注射劑的成分寫成「Calcitriol (300000IU／600000IU)」（Calcirol 600000IU Injection 36119、Devita Injection 65100、Osta D3 600000IU 162706、Osta D3 300000IU 166938；IU 劑量是維生素 D3，calcitriol 以 mcg 計），drug_mapping.csv 照成分欄對到 DB00136 而收進 calcitriol。
  排除表 `config/license_exclusions.json`（每筆附資料集原文依據與理由）；`scripts/exclude_bundle_records.py` 依表把品項從 `data/bundles/<藥>/drug_bundle.json` 的 tfda.records 移到 tfda.excluded_records、total_matches 扣掉（已扣的號記在 tfda.excluded_ids，可重複執行；`--check` 只列）；`src/intxgnn/collectors/infda.py` 收集時也照表排除（依 drugbank_id）；`.github/workflows/license-refresh.yml` 在 license_refresh 前先跑這支。
  calcitriol 證據包 records 20→19（只有 36119 存進證據包）、total_matches 90→86；證據包 local_regulatory 照 refresh_pack_regulatory 重算（dosage_forms_by_route 的「packet of 6 injections」一併拿掉）；概覽狀態列／張數列 at least 20→19、程式表少一列、description 句尾照快照重算。
  正文劑型表「Injectable | 1 ml ampoule; packet of 6 injections」以 `in-lic-20261124c-calcitriol-2` 更正。資料集另有「Calcitriol (200／500／1000IU)」與鈣劑的複方（Mitocal-CCM 134767、135450，New Sunbless C 151591，Retencal-Plus 187830）同樣疑似維生素 D3 錯植，沒存進證據包，這次沒列進排除表（要人決定）。
  證據包更新經 data-overlay 推進 Release。
- B. 整頁沒有市場段落的公開頁（chlorpheniramine、docusate、ranolazine）：`scripts/sync_license_tables.py` 加 add_section（照 JpTxGNN 第二輪），在「## Safety Considerations」之前（沒有就 Conclusion and Next Steps、Disclaimer 之前）補「## India Market Information」與程式表；noindex 頁（nicotinamide、urea）與證據包沒有紀錄的頁不補。PAGE_NOTE 放行段落標題行；gate（licenses.py page_problems，第 18 項）擋「公開頁有證據包紀錄卻沒有市場段落」。
- C. 待查清單「部分收錄頁的單方說法」147 句（136 頁）：照 2026-11-06 做法只刪「single-ingredient」字樣（「as a single-ingredient product」等片語一併拿掉），其他文字與數字不動（部分收錄頁照 B 規則不改張數），每句一筆 `in-lic-20261124c-<藥>-N`，待查標 resolved（附 record_ids）。calcitriol 那句因 A 存下的紀錄剩 19 筆，改成不寫張數（「show no cancelled licences」）。
- 驗證：apply --check 0、rewrite_license_counts --check 0、sync_license_tables --check 0、checker 全量前後 0、gate exit 0；寬偵測（公開頁正文 single-ingredient／no combination 字樣、證據包存下紀錄有複方）剩 9 句，都是藥理概述（「a single-ingredient vitamin」）、有保留的句子（ofloxacin、salbutamol、norfloxacin）、clonazepam「single-ingredient and combination-containing products」或已判定的 diatrizoate，不改。
