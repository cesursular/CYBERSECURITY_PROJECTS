import pandas as pd
import re

# Log dosyasını oku
with open('log.txt', 'r') as file:
    logs = file.readlines()

# Logları dataframe'e dönüştürme
log_data = []
for log in logs:
    match = re.match(r'(\d+-\d+-\d+ \d+:\d+:\d+) (\w+) (.+)', log)
    if match:
        log_data.append(match.groups())

df = pd.DataFrame(log_data, columns=['timestamp', 'log_level', 'message'])

# Logları göster
print("All Logs:\n", df.head())

# Belirli bir seviyedeki logları filtreleme (ör. ERROR)
error_logs = df[df['log_level'] == 'ERROR']
print("Error Logs:\n", error_logs)

# Anomali Tespiti: Ardışık başarısız oturum açma denemeleri
failed_logins = df[df['message'].str.contains('Failed login attempt')]
print("Failed Login Attempts:\n", failed_logins)

# Rapor oluşturma
with open('report.txt', 'w') as report_file:
    report_file.write("Log Analysis Report\n")
    report_file.write("====================\n")
    report_file.write("Total Logs: {}\n".format(len(df)))
    report_file.write("Error Logs: {}\n".format(len(error_logs)))
    report_file.write("Failed Login Attempts: {}\n".format(len(failed_logins)))
    report_file.write("\nDetailed Error Logs:\n")
    report_file.write(error_logs.to_string(index=False))
    report_file.write("\n\nDetailed Failed Login Attempts:\n")
    report_file.write(failed_logins.to_string(index=False))

print("Log analysis complete. Report saved to 'report.txt'.")
