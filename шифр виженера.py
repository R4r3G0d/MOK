#Текст с удаленными пробелами и знаками препинания
c='snwuzzujsnmbjcdrbsyieokgncinzzuekxbshzslzwanluvsgvkrzsnqnrcbjabianqeydocnkiozzuawjeydocneyhvsmryntknmbsaqonodiruzbuvyzzzuusqiakbwsjminwsnqokbmcdxjaonbuhbrbarbampsunsnefqrbutlqaqonodiwaiqavworzuvbjiwaiqavguwqjqdrqqtoqrzzujsrzshcdrbsbqounshiguwbjabgaqwkspxyhzzazwsjminmmqneysrbypkqoykdafrcbjcquoqutbspfuagrbskasmafkqjjifrbsdibrifmqnrbskqjjifritreanpspqqkcxuvspanoyjhcxuysnzbszzuuamqqyqslaconarqynunssnakguvwybyzxqiibjchiabkbsmiakbwsjminqdibrifzvscosnekukbskzoxbutjdaknzslzdhiuwinkqsmzypqqkcxuvbjiguwruzbuvwaiqavqjqdrxyhzzazwsjminynesudshwruzbuvknzzuusqqqynygnadjbjiwhwjranajemzzakbstyokbstskvexzbjiworzuvbuhbanhhixuarrbsxjaonbuhbyifkuzsxdmysrbypqqncbarjdqwapruqdrbsbqounshibaprubampsunqkvaiprutfazzuvbjanwkknmnsvcajadrzapsrqwmiuwinkiqfobyaqokgoitayknabocnanhkcknekpinkibukbmeankbojrfimmihrchuzshykniguwrunorb'
k=[21, 7, 19] #преположив, что zzu - это the, мы нашли ключ c(i)=m(i)*K(i mod n)(mod 26), 
#пример z[25]=t[19]*k(i=4)(mod26), k=15. формула расшифровки m(i)=c(i)*K(i mod n)^-1(mod 26)  
# для расшифровки надо найти обратное к 15 по модулю 26,
#это 7 - номер буквы ключа, остальные по аналогии
alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = ''
for i in range(0, len(c), 1):
    a = 0
    for j in range(0, len(alphabet), 1):
        if c[i] == alphabet[j]:
            a = j
    tmp=(a*k[i%3])%26
    answer+=alphabet[tmp]
print(answer)
