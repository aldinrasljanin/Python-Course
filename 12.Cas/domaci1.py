# 1. Napraviti funkciju koja vraca povrsinu pravougaonika na osnovu unetih argumenata.
#    Odnosno povrsinu kvadrata ako su dva data argumenta jednaka.

def povrsina(x,y):
    if x !=y:
        return(f"Povrsina pravougaonika je {x * y}.")
    return(f"Povrsina kvadrata je {x ** 2}.")

print(povrsina(5,4))
print(povrsina(8,8))