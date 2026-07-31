import pandas as pd

def analyse_medicore_data(file_path):
    print("=========================================")
    print("🏥 MEDICORE INFRASTRUCTURE DATA ANALYSIS")
    print("=========================================\n")
    
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # 1. Basic Dataset Info
    print(f"Total Monitoring Records: {len(df)}")
    print(f"Number of VMs Monitored: {df['vm_id'].nunique()}")
    
    # 2. Server Role Averages (CPU & Memory)
    print("\n[+] Average Resource Usage by Server Role:")
    role_stats = df.groupby('vm_role')[['cpu_usage_pct', 'memory_usage_pct', 'failed_ssh_logins']].mean().round(2)
    print(role_stats)
    
    # 3. Security & Incident Analysis
    print("\n[+] Infrastructure Incidents Detected:")
    incidents = df[df['incident_flag'] == 1]
    print(incidents['incident_type'].value_counts().to_string())
    
    # 4. Critical Anomaly Detection (Max CPU Spike)
    max_cpu_idx = df['cpu_usage_pct'].idxmax()
    critical_event = df.iloc[max_cpu_idx]
    
    print("\n[+] CRITICAL ALERT: Highest CPU Spike Recorded")
    print(f"Date/Time:    {critical_event['timestamp']}")
    print(f"Server ID:    {critical_event['vm_id']}")
    print(f"CPU Usage:    {critical_event['cpu_usage_pct']}%")
    print(f"Event Cause:  {critical_event['incident_type']}")
    print("=========================================")

if __name__ == "__main__":
    analyse_medicore_data("medicore_monitoring_data.csv")
