class Solution(object):
    def palindrome(self,s):
        n = len(s)
        if not n:
            return True
        if n%2 == 0:
            if s[0:n/2] == s[n/2:][::-1]:
                return True
            else:
                return False
        else:
            if s[0:n/2] == s[n/2+1:][::-1]:
                return True
            else:
                return False
    def process(self,a,b):
        # default len(a)<=len(b)
        if self.palindrome(b[:len(b)-len(a)]) and b[len(b)-len(a):]==a[::-1]:
            return True
        else:
            return False
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                if len(words[i])<=len(words[j]):
                    # self.process(words[i],words[j])
                    if self.process(words[i],words[j]):
                        res.append([i,j])
                else:
                    if self.process(words[j],words[i]):
                        res.append([j,i])
        return res
    def palindromePairs1(self, words):
        wordict = {}
        res = []
        for i in range(len(words)):
            wordict[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
                    res.append([i,wordict[tmp1[::-1]]])
                if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    res.append([wordict[tmp2[::-1]],i])
        return res

a = Solution()
s = 'aa'
b = 'abba'
print a.palindrome(s)
print a.palindrome(b)
k = 'aa'
b = 'ba'
print a.process(k,b)
words = ["fiecghdihdefcdgggijg","fhigideedaecjcj","ccdjhfefidh","jccedjfidfhig","jgbegfffjgh","edccbhcffbhdf","cagce","bbffjfccdchjaiehihah","dajh","hdgdhdj","ibieidg","jh","hebbbiagefhbbdh","eabcefihefibbfhebii","chcjdcjccbffiabahcjg","djceheiggcjeiifc","fdjjbehfdifiacai","aacgeechagd","eejhgfgahabjeb","h","hghiibbbihiidfch","cjg","da","hcdiiibbggibjc","fbcag","deaaajihhciigf","ahgeebbefai","ehjjehaag","cj","accghdaaifib","jjehdeiedejidd","hdgiddfiahgjhjihfhd","cjjibhihb","gfjeehfffiihj","fhicej","bchhicidieaicgeaeaej","jfeih","ccfcgfcehfia","fahjfegabhdfdhhdhbb","fgadddf","bfgdfi","dedchbhcbbajgfgggcd","ccdahcibieijjjjbef","bfbceegfb","hagig","aiifbjg","bihcfgfj","bfcebeejhgeh","dfjheejcgee","dfe","gbha","jaiiihhfadbe","gcbedchijidj","edc","acjgafcb","hjacidh","bgchhfeahih","cdabcabfijjchdgi","abjfh","egbhdaebcfjed","cfgbjgbbhdeaghb","igibebhbhgbb","giajijc","hieadcgaibfeefffebc","cdbjjgeaecacbfcggjja","fcacehgaibfd","ibcccjb","aeg","fjggidhiadejhfa","ibjbgjdea","dcfadjejajjehfagi","hbdjgdg","djbedea","hcg","hgcbefibcde","c","feeiccehjjefgh","faahdjhee","hg","eif","idgciijjeaefh","hejfh","dci","fjchiiahdcab","e","gcfchbebggiege","fihgic","dbeghfedbjehdaf","eiiccjdhhjgdgdbdacf","ifhbghdggajhdi","eihhahaeije","dgfbfheafcgadeh","jjacd","ebedhjadeebcghgeggfe","iiabagfhbgfi","iadcebdbjbeg","ifjj","aihaehfcffihjbc","jfihajifidihjhhd","fgbj","ijjacfjjcbbgjce","gf","iddf","gghhciijhh","afiabafdf","j","fcehcdbbjjgjjjd","geggef","ggadbechbbdbici","dhjijdbge","cbdhj","adgcefdbg","dhiei","jjjhged","hdhdacddeeebhcdheei","ghggcaj","ijhbabcjgjahc","cbaahcdhgbchbdbdaejj","jgjdcgbecbfhggjgbei","eb","hdhffaafhiecbccjb","jfbafdbdbdjgjiaabi","eghgdiahabebc","djfdd","acgddhjhdhihgfi","hchgegfdhj","cchbcedf","gcjjaehjhihbaabd","jjifhadabbjbhigbeh","eghjghdabed","bahag","hechejcejdbjjafhcg","aieaiecaaajbhjacfdg","d","gfiahddjiedjabjcgjdg","iieadfehfjfa","cijde","abeachjfcjgfjajceja","geaficjj","hj","f","gdiejghjgdi","bfjhifdhbdiiaiai","cecfh","faeggf","fhffg","dibahgddia","icidefafb","giedfeaiciehaeebd","ihfibggca","dcggi","ad","haf","hjaejjij","acbddbj","cgfidfieccje","ia","jedggjifcjheca","gfbgcdabahifhfeajfb","jdjehafbfcbhcjge","aa","dbghbcacdce","i","eccicaagdbgedbcci","gbhbdei","bdd","dbbjfiecbgdjieaadfh","fdjffc","hfjaijabbigajdhahf","fhfhhhhgf","dgb","chef","bcebhaiejbfbicidgfh","aegfdcdhgaj","bjdfiiegih","hcihbigicagdhhiaj","acgccddgabgjejehbc","cbcfjhccbjig","dhf","dgihebgefc","adjfjhjecbcgda","hadjfg","hfgghccdcfca","jbgcaeahfijifdhggh","jibhjdiiic","eieffgicdbahdcaajec","bg","bbjhaacgjacbfhhejah","chbfhaifcdacedeifcce","iecfdciadfbjcaffb","afbaefgdfggbhceca","ced","gciihhffech","ahgjhgejdeaaegic","fffjjghahhibdec","djfihfcadcceifaa","chjhjg","hdbfhcfehbjadccda","jdahifhihefbfgdbhg","jjhccbjacgfgad","ae","ccejcgdcdhifbgf","biacbegih","gfihgigejijbffe","eagebgefj","ibjagb","fedegdacdj","efdbfbhfhdechihhbgjb","gbajeehhgffafhccfab","dbeehajfhbig","faaacdbibfhf","gcdc","idcfgdiaibfb","jegfeicjffeiigcg","aiichehbh","gjhhjeddbfhjdihabg","aebeajgdeb","dfhjadhacfbfa","igffgeeieecf","gdheebgbcd","dijfhdjiba","gfegfiic","fbija","jieijdgfbhcdjeh","aebf","cd","ghjbehdicejjhc","aid","ed","gia","chhddcfgfj","cdbcafbji","fig","egjbicicdjdaabaghdji","iciifdd","cdidd","heigcffegcbihdhbfj","bjihbcafe","ijibcfiaidaadfcchchb","djdb","ghebagjffbdj","fhiba","cggcjccfjfdie","jeh","iihaajgfd","bajfahghjcchi","hefiaggbgg","bhfcegcjfiagdadffhfe","cbcgifeajigecebjd","jahiifiiadhfbjieiig","hghfjcbjhehebfghbdib","jfaaaij","edgjifhij","ffbicfhhahfjbcjdhaj","dia","dfjeijfchhdcfeb","hecgbjbbhbfdifhade","iijcfjifbjh","ag","chha","ifjajicdfiicjgg","diehdbbhbd","icgfcbfadiag","gceedbecfdaeihd","bacijjce","dhfe","jd","abfjhcabifgcjbjf","ja","ccabadddhdgjfaeh","cei","hc","fhacbhhcgjhjdhig","cgibbcbbe","b","fiehhggj","jadhcefcabdidcjjcfe","ebjadbb","cegffhh","ff","abhhi","egcdbigibfa","gch","dgdc","jhijededca","geji","hdcjicijcfhafjfhcfbb","ceiiccfbfgfbccgf","cgdgggjhbhchecbjea","hb","cebcjbebecfgaigd","ehbjai","aceegjgb","ciace","djdij","bdagjcbghgedjfeehbad","hbahgjbj","bghdgfa","dhbcigjd","jhaicfbcjgjjbbacf","eicifdeefiejhidb","ce","aecgc","ddhiefcbhejbghc","echjfgg","dejhdgfjca","bfbdhge","cebhfaiahfd","chhb","bbf","bgieee","jhbecgij","jgjhbhgc","bj","gdifci","djegcaaifaigg","ddbaffhaighaahbj","cgcedfcbecgfbfab","jdgbcaafcaecijcbcf","efgfjfjbghcdcagbg","fdecgadedcegihefhi","jagbefjjgjeagfdhhdf","bcacfhecchjdadhjid","jfddgbciaehjaab","dheede","aggjfjgfgjfcccgdidjg","fbcfdgbcibbdcic","cdfjfihagihc","eajcfbghc","hib","eghagcfcg","fbfgca","djbebjdbcfhbj","iaee","djbghccgajidadcbcbhh","giefbjfjidb","hcajg","egadaefa","abaccjg","bbfehi","agahgfdffdeeiebiggb","bcfci","a","ddagjhbeejgbchgh","cfdhdffdjbchf","chgehfagcdjgeihgchie","ea","iddjbcdii","bcjgdhahjiefcgjahdj","ecbcahjcce"]
print a.palindromePairs(words)
