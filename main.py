from numpy import double
import win32api
import shutil

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Verfügbare Laufwerke:")
print(drives)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for entry in drives:
    if 'D:\\' in entry:
        print(entry, "ist ein Laufwerk")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    else:    
        total, used, free = shutil.disk_usage(entry)
        print("Festplatte", entry)
        warning = "{:.2f}".format(100 / total * used)
        freespace = "{:.2f}".format(100 / total * free)
        print("Total: %d GiB" % (total // (2**30)))
        print("Used: %d GiB" % (used // (2**30)),"(",warning,"%)")
        print("Free: %d GiB" % (free // (2**30)),"(",freespace,"%)")
        if double(warning) >= double(85):
            print("Warnung : Festplatte", entry, "fast voll!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
