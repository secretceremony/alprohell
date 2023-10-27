def calculate_time(file):
    
    with open("waktu.txt","r") as file:
        lines = file.readlines()

    total_waktu = 0 
    jumlah_data = 0 
    
    for line in lines[1:]: 
        parts = line.split(', ') 
        if len(parts) == 2:
            time_str = parts[1] 
            time_parts = time_str.split()  
            if len(time_parts) == 4:
                mins = int(time_parts[0]) 
                secs = int(time_parts[2]) 
                total_waktu += mins * 60 + secs 
                jumlah_data += 1 

    if jumlah_data > 0:
        rata_rata_waktu = total_waktu / jumlah_data  
    else:
        rata_rata_waktu = 0

    return total_waktu, rata_rata_waktu

total_waktu, rata_rata_waktu = calculate_time(license)
print("Total Waktu Pengerjaan:", total_waktu, "detik")
print("Rata-rata Waktu Pengerjaan:", rata_rata_waktu, "detik")
