def main():
    v = feet2meter(input("Сколько футов:"))
    #print(f"Это будет"{v:.2f}.format(v) "метров.")

def feet2meter(v):
	# Здесь будет ваш код
    t = float (v.replace("ft",""))
    m = (t*0.3048)
    k = (f"{m:.2f}")
    print ("Это будет " + k + " метров.", end='\n')
main()