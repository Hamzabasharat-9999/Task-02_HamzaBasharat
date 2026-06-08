import pandas as pd
import numpy as np

print("🔬 Initializing DecodeLabs EDA Forensic Engine...\n")

# Load your clean dataset
file_name = "Cleaned_Dataset_Project1.csv"

try:
    df = pd.read_csv(file_name)
    print(f"📊 Dataset successfully loaded. Shape: {df.shape[0]} rows, {df.shape[1]} columns.\n")
    
    # ----------------------------------------------------
    # MILESTONE 1: DESCRIPTIVE STATISTICS (CENTER OF GRAVITY)
    # ----------------------------------------------------
    print("==================================================")
    print("🧠 MILESTONE 1: Calculating Centers of Gravity")
    print("==================================================")
    
    # Target our primary numerical variables
    num_cols = ['Quantity', 'UnitPrice', 'TotalPrice']
    
    # Generate the Five-Number Summary
    summary = df[num_cols].describe()
    print(summary.to_string())
    print("\n✅ Five-Number Summaries extracted successfully.")

    # ----------------------------------------------------
    # MILESTONE 2: OUTLIER EXTRACTION (THE IQR METHOD)
    # ----------------------------------------------------
    print("\n==================================================")
    print("🕵️‍♂️ MILESTONE 2: Executing Outlier Forensic Audit")
    print("==================================================")
    
    # Using IQR method as required for business data
    for col in ['TotalPrice', 'Quantity']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Flagging the anomalies
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"🔍 Column '{col}':")
        print(f"   -> IQR: {IQR:.2f} | Expected Range: [{lower_bound:.2f} to {upper_bound:.2f}]")
        print(f"   -> Flagged Anomalies (Signals): {len(outliers)} rows identified out of {len(df)}.")
    
    # ----------------------------------------------------
    # MILESTONE 3: CORRELATION ANALYSIS
    # ----------------------------------------------------
    print("\n==================================================")
    print("🔗 MILESTONE 3: Mapping Linear Relationships")
    print("==================================================")
    
    # Calculate Pearson Correlation Matrix
    correlation_matrix = df[num_cols].corr(method='pearson')
    print("Pearson Correlation Coefficient Matrix (r):")
    print(correlation_matrix.round(4).to_string())
    
    print("\n🎯 FORENSIC AUDIT COMPLETE! Ready for Executive Review.")

except FileNotFoundError:
    print(f"❌ Error: Could not find '{file_name}' in this folder. Make sure it's in DeCodesLab!")