import pandas as pd
import io

tcs_infosys_csv = """company,fiscal_quarter,quarter_end_date,revenue_inr_cr,revenue_usd_mn,headcount,source_doc,source_url
TCS,Q1 FY22,2021-06-30,45411,6154,509058,TCS Press Release Q1 FY22,https://www.tcs.com/investor-relations
TCS,Q2 FY22,2021-09-30,46867,6333,528748,TCS Press Release Q2 FY22,https://www.tcs.com/investor-relations
TCS,Q3 FY22,2021-12-31,48885,6524,556986,TCS Press Release Q3 FY22,https://www.tcs.com/investor-relations
TCS,Q4 FY22,2022-03-31,50591,6696,592195,TCS Press Release Q4 FY22,https://www.tcs.com/investor-relations
TCS,Q1 FY23,2022-06-30,52758,6780,606331,TCS Press Release Q1 FY23,https://www.tcs.com/investor-relations
TCS,Q2 FY23,2022-09-30,55309,6877,616171,TCS Press Release Q2 FY23,https://www.tcs.com/investor-relations
TCS,Q3 FY23,2022-12-31,58229,7075,613974,TCS Press Release Q3 FY23,https://www.tcs.com/investor-relations
TCS,Q4 FY23,2023-03-31,59162,7195,614795,TCS Press Release Q4 FY23,https://www.tcs.com/investor-relations
TCS,Q1 FY24,2023-06-30,59381,7226,615318,TCS Press Release Q1 FY24,https://www.tcs.com/investor-relations
TCS,Q2 FY24,2023-09-30,59692,7210,608985,TCS Press Release Q2 FY24,https://www.tcs.com/investor-relations
TCS,Q3 FY24,2023-12-31,60583,7281,603305,TCS Press Release Q3 FY24,https://www.tcs.com/investor-relations
TCS,Q4 FY24,2024-03-31,61237,7363,601546,TCS Press Release Q4 FY24,https://www.tcs.com/investor-relations
TCS,Q1 FY25,2024-06-30,62613,7505,606998,TCS Press Release Q1 FY25,https://www.tcs.com/investor-relations
TCS,Q2 FY25,2024-09-30,64259,7670,612724,TCS Press Release Q2 FY25,https://www.tcs.com/investor-relations
TCS,Q3 FY25,2024-12-31,63973,7539,607354,TCS Press Release Q3 FY25,https://www.tcs.com/investor-relations
TCS,Q4 FY25,2025-03-31,64479,7465,607979,TCS Press Release Q4 FY25,https://www.tcs.com/investor-relations
Infosys,Q1 FY22,2021-06-30,27896,3782,267953,Infosys Fact Sheet Q1 FY22,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q2 FY22,2021-09-30,29602,3998,279617,Infosys Fact Sheet Q2 FY22,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q3 FY22,2021-12-31,31867,4250,292067,Infosys Fact Sheet Q3 FY22,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q4 FY22,2022-03-31,32276,4280,314015,Infosys Fact Sheet Q4 FY22,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q1 FY23,2022-06-30,34470,4444,335186,Infosys Fact Sheet Q1 FY23,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q2 FY23,2022-09-30,36538,4555,345218,Infosys Fact Sheet Q2 FY23,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q3 FY23,2022-12-31,38318,4659,346845,Infosys Fact Sheet Q3 FY23,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q4 FY23,2023-03-31,37441,4554,343234,Infosys Fact Sheet Q4 FY23,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q1 FY24,2023-06-30,37933,4617,336294,Infosys Fact Sheet Q1 FY24,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q2 FY24,2023-09-30,38994,4718,328764,Infosys Fact Sheet Q2 FY24,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q3 FY24,2023-12-31,38821,4663,322663,Infosys Fact Sheet Q3 FY24,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q4 FY24,2024-03-31,37923,4564,317240,Infosys Fact Sheet Q4 FY24,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q1 FY25,2024-06-30,39315,4714,315332,Infosys Fact Sheet Q1 FY25,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q2 FY25,2024-09-30,40986,4894,317788,Infosys Fact Sheet Q2 FY25,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q3 FY25,2024-12-31,41764,4939,323379,Infosys Fact Sheet Q3 FY25,https://www.infosys.com/investors/reports-filings/quarterly-results.html
Infosys,Q4 FY25,2025-03-31,40925,4730,323578,Infosys Fact Sheet Q4 FY25,https://www.infosys.com/investors/reports-filings/quarterly-results.html"""

wipro_hcltech_csv = """company,fiscal_quarter,quarter_end_date,revenue_inr_cr,revenue_usd_mn,headcount,source_doc,source_url
Wipro,Q1 FY22,2021-06-30,18250,2414.5,209890,Wipro Q1 FY22 Press Release,https://www.wipro.com/newsroom/press-releases/2021/wipro-reports-results-for-the-quarter-ended-june-30-2021/
Wipro,Q2 FY22,2021-09-30,19670,2580.0,221365,Wipro Q2 FY22 Press Release,https://www.wipro.com/newsroom/press-releases/2021/wipro-reports-results-for-the-quarter-ended-september-30-2021/
Wipro,Q3 FY22,2021-12-31,20310,2639.7,231671,Wipro Q3 FY22 Press Release,https://www.wipro.com/newsroom/press-releases/2022/wipro-reports-results-for-the-quarter-ended-december-31-2021/
Wipro,Q4 FY22,2022-03-31,20860,2721.7,243128,Wipro Q4 FY22 Press Release,https://www.wipro.com/newsroom/press-releases/2022/wipro-reports-results-for-the-quarter-ended-march-31-2022/
Wipro,Q1 FY23,2022-06-30,21530,2735.5,258574,Wipro Q1 FY23 Press Release,https://www.wipro.com/newsroom/press-releases/2022/wipro-reports-results-for-the-quarter-ended-june-30-2022/
Wipro,Q2 FY23,2022-09-30,22540,2797.7,259179,Wipro Q2 FY23 Press Release,https://www.wipro.com/newsroom/press-releases/2022/wipro-reports-results-for-the-quarter-ended-september-30-2022/
Wipro,Q3 FY23,2022-12-31,23230,2803.5,258744,Wipro Q3 FY23 Press Release,https://www.wipro.com/newsroom/press-releases/2023/wipro-reports-results-for-the-quarter-ended-december-31-2022/
Wipro,Q4 FY23,2023-03-31,23190,2823.0,256921,Wipro Q4 FY23 Press Release,https://www.wipro.com/newsroom/press-releases/2023/wipro-reports-results-for-the-quarter-ended-march-31-2023/
Wipro,Q1 FY24,2023-06-30,22830,2778.5,249758,Wipro Q1 FY24 Press Release,https://www.wipro.com/newsroom/press-releases/2023/wipro-reports-results-for-the-quarter-ended-june-30-2023/
Wipro,Q2 FY24,2023-09-30,22520,2713.3,244707,Wipro Q2 FY24 Press Release,https://www.wipro.com/newsroom/press-releases/2023/wipro-reports-results-for-the-quarter-ended-september-30-2023/
Wipro,Q3 FY24,2023-12-31,22210,2656.1,240234,Wipro Q3 FY24 Press Release,https://www.wipro.com/newsroom/press-releases/2024/wipro-reports-results-for-the-quarter-ended-december-31-2023/
Wipro,Q4 FY24,2024-03-31,22210,2657.4,234054,Wipro Q4 FY24 Press Release,https://www.wipro.com/newsroom/press-releases/2024/wipro-reports-results-for-the-quarter-ended-march-31-2024/
Wipro,Q1 FY25,2024-06-30,21960,2625.9,234391,Wipro Q1 FY25 Press Release,https://www.wipro.com/newsroom/press-releases/2024/wipro-reports-results-for-the-quarter-ended-june-30-2024/
Wipro,Q2 FY25,2024-09-30,22300,2660.1,233889,Wipro Q2 FY25 Press Release,https://www.wipro.com/newsroom/press-releases/2024/wipro-reports-results-for-the-quarter-ended-september-30-2024/
Wipro,Q3 FY25,2024-12-31,22320,2629.1,232732,Wipro Q3 FY25 Press Release,https://www.wipro.com/newsroom/press-releases/2025/wipro-reports-results-for-the-quarter-ended-december-31-2024/
Wipro,Q4 FY25,2025-03-31,22500,2596.5,233346,Wipro Q4 FY25 Press Release,https://www.wipro.com/newsroom/press-releases/2025/wipro-reports-results-for-the-quarter-ended-march-31-2025/
HCLTech,Q1 FY22,2021-06-30,20068,2720,176499,HCLTech Q1 FY22 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q2 FY22,2021-09-30,20655,2790,187634,HCLTech Q2 FY22 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q3 FY22,2021-12-31,22331,2977,197777,HCLTech Q3 FY22 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q4 FY22,2022-03-31,22597,2993,208877,HCLTech Q4 FY22 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q1 FY23,2022-06-30,23464,3025,210966,HCLTech Q1 FY23 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q2 FY23,2022-09-30,24686,3082,219325,HCLTech Q2 FY23 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q3 FY23,2022-12-31,26700,3244,222270,HCLTech Q3 FY23 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q4 FY23,2023-03-31,26606,3235,225944,HCLTech Q4 FY23 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q1 FY24,2023-06-30,26296,3200,223438,HCLTech Q1 FY24 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q2 FY24,2023-09-30,26672,3225,221139,HCLTech Q2 FY24 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q3 FY24,2023-12-31,28446,3415,224756,HCLTech Q3 FY24 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q4 FY24,2024-03-31,28499,3430,227481,HCLTech Q4 FY24 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q1 FY25,2024-06-30,28057,3364,219401,HCLTech Q1 FY25 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q2 FY25,2024-09-30,28862,3445,218621,HCLTech Q2 FY25 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q3 FY25,2024-12-31,29890,3533,220755,HCLTech Q3 FY25 Financial Results,https://www.hcltech.com/investors/results-reports
HCLTech,Q4 FY25,2025-03-31,30246,3498,223420,HCLTech Q4 FY25 Financial Results,https://www.hcltech.com/investors/results-reports"""

techm_csv = """company,fiscal_quarter,quarter_end_date,revenue_inr_cr,revenue_usd_mn,headcount,source_doc,source_url
Tech Mahindra,Q1 FY22,2021-06-30,10198,1383.6,126263,Tech Mahindra Q1 FY22 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q2 FY22,2021-09-30,10881,1472.6,141193,Tech Mahindra Q2 FY22 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q3 FY22,2021-12-31,11451,1533.5,145067,Tech Mahindra Q3 FY22 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q4 FY22,2022-03-31,12116,1608.1,151173,Tech Mahindra Q4 FY22 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q1 FY23,2022-06-30,12708,1632,158035,Tech Mahindra Q1 FY23 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q2 FY23,2022-09-30,13129,1638,163912,Tech Mahindra Q2 FY23 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q3 FY23,2022-12-31,13735,1668,157068,Tech Mahindra Q3 FY23 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q4 FY23,2023-03-31,13718,1668,152400,Tech Mahindra Q4 FY23 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q1 FY24,2023-06-30,13159,1601,148297,Tech Mahindra Q1 FY24 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q2 FY24,2023-09-30,12864,1555,150604,Tech Mahindra Q2 FY24 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q3 FY24,2023-12-31,13101,1573,146250,Tech Mahindra Q3 FY24 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q4 FY24,2024-03-31,12871,1548,145455,Tech Mahindra Q4 FY24 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q1 FY25,2024-06-30,13005,1559,147620,Tech Mahindra Q1 FY25 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q2 FY25,2024-09-30,13313,1589,154273,Tech Mahindra Q2 FY25 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q3 FY25,2024-12-31,13286,1567,150488,Tech Mahindra Q3 FY25 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/
Tech Mahindra,Q4 FY25,2025-03-31,13384,1549,148731,Tech Mahindra Q4 FY25 Press Release,https://www.techmahindra.com/en-in/investors/financial-results/"""

nasscom_csv = """year,sector_revenue_usd_bn,sector_employment_total,revenue_growth_pct,employment_growth_pct,source_url
FY23,245,5400000,8.4,5.7,https://nasscom.in/knowledge-center/publications/tech-september-quarterly-review-fy23
FY24,253.9,5430000,3.8,1.1,https://nasscom.in/knowledge-center/publications/strategic-review-2024
FY25,283,5800000,5.1,2.3,https://nasscom.in/knowledge-center/publications/strategic-review-2025
FY26,315,5950000,6.1,2.3,https://nasscom.in/knowledge-center/publications/strategic-review-2026"""

# Combine company dataframes
df_tcs_infy = pd.read_csv(io.StringIO(tcs_infosys_csv))
df_wipro_hcl = pd.read_csv(io.StringIO(wipro_hcltech_csv))
df_techm = pd.read_csv(io.StringIO(techm_csv))

df_company = pd.concat([df_tcs_infy, df_wipro_hcl, df_techm], ignore_index=True)
df_nasscom = pd.read_csv(io.StringIO(nasscom_csv))

# Save to CSV files in workspace
df_company.to_csv(r"c:\Users\Omkar\OneDrive\Desktop\Data Analytics Project\Revenue vs Headcount Decoupling\company_quarterly_data.csv", index=False)
df_nasscom.to_csv(r"c:\Users\Omkar\OneDrive\Desktop\Data Analytics Project\Revenue vs Headcount Decoupling\nasscom_sector_data.csv", index=False)

print(f"Company dataset shape: {df_company.shape}")
print(f"NASSCOM dataset shape: {df_nasscom.shape}")

print("\n--- Company counts ---")
print(df_company["company"].value_counts())

print("\n--- Null check company data ---")
print(df_company.isnull().sum())

print("\n--- Null check nasscom data ---")
print(df_nasscom.isnull().sum())
