import random
from extend_mt19937_predictor import ExtendMT19937Predictor

array = [45941894538812633403521750727576904042755795333563315121398055836902922257372,86217537527657001628014860365732753983424140694810151008282211676706772784601,10681591734677395589041349621750658892415805044835618555985358343667520566301,35691699102239705066119348586711864515641670844524531302494366383878970544607,48817125933764726505806383387881847954756201104000736279371860604255291546245,58754849253009146350504207874538905239995180467823650786054557145355270689280,11606411663611367995632382718734149633881815916168989830068327078719665975852,111739917476470293321748722667838990227383294445595847907188040536990744736674,8030577869059090988292306408737913429268134983357511381570845573132066621426,27735465606725696839357495929385336279619256882437963818155680265307745634875,18704116887857184149377230425786579035584657651389500404686775159730436319175,22083433856360924286251997535356923085566451926046515203493826388824739395723,51503362063677513792700500871821382850730709079166064421858460184209357187206,108081602712458510515944540170482496935632670969193034427467382674086321190615,81573088551689675090298195676232992913027064074867779006996420091895419846652,87320776010362086325105131053482574814926990225645070599127672238428091281456,18819342542643393693624528076349669063044350195930481054836784634065386289538,2885530281883960243933404606714220675560576317086128231317169000847261865513,58396379164164087991493990861173985313943656497731993791511391934507900321880,98584342290219579901701006386078469488114973970043499545354425261015742792255,45610444544812376449263183999145584432878742874839230741800730704508316016845,10636057604198601763011066365216427896344938490790314745463500608302299012982,41127328596815308858469035970887644750800769876856631310327742234857545604360,50802446361056140806627822783424851427917698607447846653355069244683474032332,76050841821290173426589979241075812909322175318978795172882928167842754190849,73768809503530919252369989783582536536616174765246623213034069402327865704307,2564396239271471318899849393791419211055214404798565825728947499033679121026,73795874778522222198853299367554195598812782637448470952461791059254717040132,49048632594465890882127367997327962328735453469471480240723524136258030991639,110658661979031074854797559403592145143737916450267662918167741284102786120891,20765016534866036605691186893541147563418877260926766983845258842379272652626,48465995790309989114993984523767788253149641799085942502962459493856221655219,32430192437679280231685148678945936096652995518711819043737010399629628021215,94614041873683689864616866861545463520850106626553649996274658773654274215376,75902222748046820443413750465430036876122897106320346923249835661296752550063,87515588052834948607861922531794614086920649171805244015415092957544383852113,37102891185680110651549266008030984529327824355280951683357579242554439143937,22336840308634044757317360363059123515965024372415073053023472290293762372699,47601634143814046401311555946325029207493755607491409578857948044417861777124,2079555232238866385774256061114340502187249012759954618705810744983260544640,42006636329001038324639521025046487963933495655440377628162183329269842522273,100140905067199500992284399934125567279679889413858706801165047495500007780373,52104747023891176358667614035490825460755188064279450152245222155661407737508,76932279479779221744101096027032138166960999973680726166663680781653851519801,21884203167612992905292081282079046366019122323570586156627634625655304360533,57566416440179447675284596334528803844852202741698779967430546740460475408535,46003083851751053727552234146846375214135918417941516311915434888418523555767,109831826523631146324635516737349229785242410713676366135984447142249743659340,65724874854090139833805930773729652790500250580904307054713862058327590130663,64318392857105536483028838255826678730313394083726734647320055117713240086011,66477079372066465129042227946022249523012348341074248435058894232577892042175,36268252979530877175940031851383359604300107010308474570833231939645022577333,104863180888783129140529561151373162858818072955604780055550023891405602903403,104256426890057213499637184390606311280206158144839272599853064296153513358676,80611833813758074331731760289343708761128542097645725843617189381502907436058,70029954336602149080799853671955395150313568683476671867395793936282074696676,30204465229076982408933879946034526620205635147752707669042288424207378038476,48691692504537976942060124464739801807740085405079810792520106742451546103723,109928764072370426656554081590901224248054301073932043798968029733525145592594,48859992947843500622276714790676878958151569392961513083854812931772914360162,20325353593849439653484659466423295396925070135590260417951450523891973277786,52525950983657423395083176614779498849483178047839876383739836321460890373449,50887085077305217180236947593708833977644929997776932760736890911454682732033,111437560203452654281099614062792916955501221214974565401433335995667446059592,103426730312489212434256007660238392615676736278051912792777779039019883645424,42175840665985229266112091677085437574415345717894339769782699186818750585343,11692795918708249108726651973333587563198639224428443070258441482675934517349,3247318614825591372484553192861568413424580844435120172859508939898591284519,76474847286045613449554845685148889944625791615868569603970904235525011321587,16896831284243459469737577020383198519878722984500491191738689712826710181732,102442905298264741725818604771598583512653315836890886354781668234843452104691,111701666216436708617136506531168800601190167972914632887469366438541213420582,20941650668512505163623576104687877398691730290764733300506485866152052662618,41591457425417282902270151128665485635315959696495736438651681021808044261272,70133434883735745504110991712542838093971641464609562114745009632127032309464,63223993692531521863472825698734251902397742873698518025567979430902952678779,103981248443016841358352313062417674999968512024088130486931822413793425291700,28834112402486573921440392033521735148263186359108315646473200521462654468812]
predictor = ExtendMT19937Predictor()

for i in range(78):
    predictor.setrandbits(array[i], 256)

key = predictor.predict_getrandbits(256)
print(key)