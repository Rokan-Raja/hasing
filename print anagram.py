def check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
s1 = "listen"
s2 = "silent"
s3 = "dad"
s4 = "bad"
print("s1 and s2 is:")
check(s1, s2)
print("\ns3 and s4 is:")
check(s3,s4)

