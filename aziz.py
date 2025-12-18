# Start of the program
# Identitas Pembuat Program Universitas Muhammadiyah Kendari
print("NAMA : AZIZ FAISURACHMAN") 
print("NIM : 22515020")
print("KELAS : STI_A") 
print("...") 

# Program Perhitungan Biaya Parkir dengan Ketentuan
print("<-- Program Perhitungan Biaya Parkir -->")
print("      ## Kententuan Parkir : ##")
print("       1. Mobil : Rp 5000/jam")
print("       2. Motor : Rp 2000/jam")
print("       3. Truk : Rp 10000/jam")
print("       4. Jika parkir lebih dari 5 jam, akan dikenakan biaya tambahan sebesar 10%")
print("## Mohon Patuhi Ketentuan Parkir Diatas ##")
print("...")

# input jenis kendaraaan
jenis_kendaraan = (input("masukan jenis kendaraan (mobil, motor, truk) >>> :")).lower()

#tarif Kendaraan perjam
if jenis_kendaraan == "mobil":
    tarif_per_jam = 5000
elif jenis_kendaraan == "motor":
    tarif_per_jam = 2000
elif jenis_kendaraan == "truk":
    tarif_per_jam = 10000
else:
    print("Jenis Kendaraan tidak sesuai")
    exit()

# input lama parkir
lama_parkir = int(input("masukan lama parkir (jam) >>> : "))

# rumus tarif dasar
tarif_dasar = tarif_per_jam * lama_parkir

# menghitung total biaya jika parkir lebih dari 5 jam atau tidak
biaya_tambahan = 0
if lama_parkir > 5:
    biaya_tambahan = tarif_per_jam + (tarif_dasar * 0.10)

# output rincian biaya parkir
print("+______________________________________________+")
print("|           Rincian Biaya Parkir               |")
print(f"  Jenis Kendaraan : {jenis_kendaraan}")
print(f"  Lama Parkir : {lama_parkir} jam")
print(f"  Tarif Dasar : Rp {tarif_dasar}")
print(f"  Biaya Tambahan : Rp {int(biaya_tambahan)}")
print(f"  >> Total Biaya : {int(biaya_tambahan)}")
print("| _____________________________________________|")

# End of the program