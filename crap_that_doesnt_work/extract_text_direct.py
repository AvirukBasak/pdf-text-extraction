# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
# reader = PdfReader('pdfs/TXT Mines and Minerals Act.pdf')
reader = PdfReader('pdfs/TXT Mineral Auction Amendment Rules.pdf')

for page in reader.pages:
    text = page.extract_text()
    print(text)

# printing number of pages in pdf file
print('\npage count:', len(reader.pages))

'''
SHITTY Hindi Results:

5641 GI/2023 (1) स
xxxGIDHxxx
xxxGIDExxx
अध
EXTRAORDINARY
भगII—खणड3—उ-खणड(i)
PART II—Section 3—Sub-section (i)
पधप
PUBLISHED BY AUTHORITY
ख
अध
ईदल, 1,2023
...648(अ).—य,खऔख(औय)अधय,1957 (1957
67)ीध13पतयपयगए,ख()य,2015औ
मखय,अा्:—
1. (1)इय
(2)यउ पीखप
2.ख()य, 2015 (इइ शउयगय),य5,उ-य(2),
मख
“
 य द अनय  पध  भ
उयगभ
3.उय,य9,—
(i)उ-य(1),ख
अ
No. 507] NEW DELHI, FRIDAY, SEPTEMBER 1, 2023/ BHADRA 10, 1945
सी.जी.-डी.एल.-अ.-02092023-248503
CG-DL-E-02092023-248503
2  THE GAZETTE OF INDIA : EXTRAORDINARY    [P ART II—S EC. 3(i)]
“
 य द अनय  पध  भ
उयग भ
(ii)उ-य(2),ख
अ
“
जय  य द अनय  पध  भ
बयौ  उयग भ
4.उ य ,य9  श्,मख य अ
“9ख.ध11घअधयखटी—(1)जय  ख
()
घ  रा द ख  
य ख  बयौ    य   एग।
(2)जय  मख  
()इी पि  
ॉो ड य द अनय  य  इई  ख ट ी   ए अधय ी
प अ
(ख)ऐ ि  य वयग    
रा द ख  
(3)य  जय      ए य5औ9 अध आय  प
 ी अ    औ जय   द  भ य   ऐ  प
ग।
(4)ध11घ  अध ख ट   ए य     ,य59 उ
 द जय   ग
(5)  फ  ,य    अध    जय 
 एग औ जय  ऐ अध   य10 अ
ग।
5.उ य ,य17  च्,मख य अ
“17ख.ध11घअधयदअ
ख()
 भग घ  रा द ख  
उबध भ  य ख   य   एग।
(2)जयमख
()इ पि  ी 
ो ड य द अनय  य  इई  द अ
ी  अ
(ख)ऐ ि  य वयग   
रा द ख  
वयग ।
[भगII—खणड3(i)] भ  :अध 3
(3)य  जय      ए य16औ17 अध आय  प
 ी अ    औ जय   द  भ य   ऐ  प
ग।
(4)ध11घ  अध द अ
 उग।
(5)  फ  ,य    अध     जय 
 अग यग औ जय  ऐ अध   य18 अ
द अ
[फ.
डॉ. 
:-ख()य, 2015 भ   अध भगII,ख
406(अ) ख20ई,2015 प दय गय  औ इ अ
ख18फ,2022 दय गय ।
MINISTRY OF MINES
NOTIFICATION
New Delhi, the 1 September, 2023
G.S.R. 648(E).—In exercise of the powers conferred by section 13 of the Mines and Minerals (Development
and Regulation) Act, 1957 (67 of 1957), the Central Government hereby makes the following rules further to amend
the Mineral (Auction) Rules, 2015, namely:—
1. Short title and commencement:— (1) These rules may be called the Mineral (Auction) Amendment Rules, 2023.
(2) They shall come into force on the date of their publication in the Official Gazette.
2. In the Mineral (Auction) Rules, 2015 (hereinafter referred to as the said rules), in rule 5, in sub-rule (2), the
following proviso shall be inserted, namely:—
“Provided that where details of the land is available in the Prime Minister Gati Shakti- National
Master Plan for Multi-modal Connectivity platform or land record portal of the State Government or any
other Government authority, the State Government may use such details for classification of the land.”.
3. In the said rules, in rule 9,—
(i) in sub-rule (1), in clause (a), for the words “land not owned by the State Government; and”, the following
shall be substituted, namely:—
“land not owned by the StateGovernment:
Provided that where details of the land is available in the Prime Minister Gati Shakti - National Master
Plan for Multi-modal Connectivity platform or land record portal of the State Government or any other
Government authority, the State Government may use such details for classification of the land; and”;
(ii) in sub-rule (2), in clause (b), for the words, “land not owned by the State Government; and” the following
proviso shall be substituted, namely:—
“land not owned by the State Government:
Provided that where details of the land is available in the Prime Minister Gati Shakti - National Master
Plan for Multi-modal Connectivity platform or land record portal of the State Government or any other
Government authority, the State Government may use such details for classification of the land; and”;
4. In the said rules, after rule 9A, the following rule shall be inserted, namely:—
“9B. Conduct of auction of mining lease by Central Government under section 11D.—(1) The State
Government shall intimate to the Central Government the details of all the areas or mines available with the
State Government for auction of mining lease, in respect of any mineral specified in the Part D of the First
Schedule to the Act within forty-five days of the commencement of the Mineral (Auction) Amendment Rules,
2023.
4  THE GAZETTE OF INDIA : EXTRAORDINARY    [P ART II—S EC. 3(i)]
(2) The State Government shall intimate to the Central Government regarding the following, namely:—
(a) receipt of any geological report in respect of any mineral specified in the Part D of the First Schedule
to the Act for auction of mining lease from Geological Survey of India, Mineral Exploration
Corporation Limited or any other Government or private entity, within a period of forty-five days of
receiving it;
(b) termination of mining lease or lapsing of letter of intent for mining lease in respect of any mineral
specified in the Part D of the First Schedule to the Act, within fifteen days from such termination or
lapse;
(3) The Central Government may require the State Government to provide the details specified under rules 5
and 9 for conduct of auction and the State Government shall provide such details to the Central Government
within thirty days.
(4) For conducting an auction by the Central Government for grant of mining lease under section 11D, the
provisions of rules 5 to 9, as applicable to a State Government, shall mutatis mutandis be also applicable to the
Central Government.
(5) Upon successful completion of the auction, the Central Government shall intimate the details of the
preferred bidder in the auction to the State Government and the State Government shall grant mining lease for
such area to such preferred bidder in accordance with rule 10.”.
5. In the said rules, after rule 17A, the following rule shall be inserted, namely:—
“17B. Conduct of auction of composite licence by Central Government under section 11D.—(1) The State
Government shall intimate to the Central Government the details of all the areas or mines available with the
State Government for auction of composite licence, in respect of any mineral specified in the Part D of the First
Schedule to the Act within a period of forty-five days of the commencement of the Mineral (Auction)
Amendment Rules, 2023.
(2) The State Government shall intimate to the Central Government regarding the following, namely:—
(a) receipt of any geological report in respect of any mineral specified in the Part D of the First Schedule
to the Act for auction of composite licence from Geological Survey of India, Mineral Exploration
Corporation Limited or any other Government or private entity, within a period of forty-five days of
receiving it;
(b) termination of composite licence or lapsing of letter of intent for composite licence in respect of any
mineral specified in the Part D of the First Schedule to the Act, within fifteen days from such
termination or lapse;
(3) The Central Government may require the State Government to provide the details specified under rules 16
and 17 for conduct of auction and the State Government shall provide such details to the Central Government
within thirty days.
(4) For conducting an auction by the Central Government for grant of composite licence under section 11D, the
provisions of rules 16 and 17, as applicable to a State Government, shall mutatis mutandis be also applicable to
the Central Government.
(5) Upon successful completion of the auction, the Central Government shall intimate the details of the
preferred bidder in the auction to the State Government and the State Government shall grant composite licence
for such area to such preferred bidder in accordance with rule 18.”.
  [F. No. M.VI-1/3/2023-Mines VI]
 Dr. VEENA KUMARI DERMAL, Jt. Secy.
Note:- The Mineral (Auction) Rules, 2015 were published in the Gazette of India, Extraordinary, Part II, Section 3,
Sub-section (i), vide number G.S.R. 406(E), dated the 20th May, 2015 and lastly amended, vide number G.S.R. 137(E),
dated the 18th February, 2022.
Uploaded by Dte. of Printing at Government of India Press, Ring Road, Mayapuri, New Delhi-110064
and Published by the Controller of Publications, Delhi-110054. MANOJ KUMAR VERMADigitally signed by MANOJ KUMAR VERMA Date: 2023.09.02 15:20:36 +05'30'

page count: 4
'''

'''
English Results:


cls; py .\\extract_text_direct.py
Short title and
commencement.THE MINES AND MINERALS (DEVELOPMENT AND REGULATION)
AMENDMENT ACT, 2023
NO. 16 OF 2023
[9th August , 2023.]
An Act further to amend the Mines and Minerals (Development and
Regulation) Act, 1957.
BE it enacted by Parliament in the Seventy-fourth Year of the Republic of India as
follows:—
CHAPTER I
PRELIMINARY
1. (1) This Act may be called the Mines and Minerals (Development and Regulation)
Amendment Act, 2023.
(2) It shall come into force on such date as the Central Government may, by notification
in the Official Gazette, appoint.vlk/kkj.k
EXTRAORDINARY
Hkkx  II — [k.M 1
PART II — Section 1
izkf/kdkj ls izdkf'kr
PUBLISHED  BY  AUTHORITY
lañ   19] ubZ fnYyh] cq/kokj] vxLr 9] 2023@Jko.k 18] 1945 ¼'kd½
No. 19] NEW DELHI, WEDNESDAY, AUGUST 9, 2023/SRAV ANA 18, 1945 (SAKA)
bl Hkkx esa fHkUu i`"B la[;k nh tkrh gS ftlls fd ;g vyx ladyu ds :i esa j[kk tk ldsA
Separate paging is given to this Part in order that it may be filed as a separate compilation.xxxGIDHxxx
xxxGIDExxx
jftLVªh lañ Mhñ ,yñ —(,u)04@0007@2003 —23 REGISTERED NO. DL—(N)04/0007/2003—23
MINISTRY OF LAW AND JUSTICE
(Legislative Department)
New Delhi, the 9th August, 2023/ Sravana 18, 1945  ( Saka )
The following Act of Parliament received the assent of the President on the
9th August, 2023 and is hereby published for general information:—
सी.जी.-डी.एल.-अ.-10082023-247989
CG-DL-E-10082023-247989
सी.जी.-डी.एल.-अ.-10082023-247989
CG-DL-E-10082023-247989
सी.जी.-डी.एल.-अ.-10082023-247989
CG-DL-E-10082023-247989
2 THE GAZETTE OF INDIA EXTRAORDINARY [P ART II—
2. In section 3 of the Mines and Minerals (Development and Regulation) Act, 1957
(hereinafter referred to as the principal Act), in section 3,—
(i) after clause ( aa), the following clause shall be inserted, namely:—
'(aaa) "exploration licence" means a licence granted for undertaking
reconnaissance operations or prospecting operations or both in respect ofminerals specified in the Seventh Schedule;';
(ii) in clause ( ae), after the words "composite licence", the words ", exploration
licence" shall be inserted;
(iii) for clause ( ha), the following clause shall be substituted, namely:—
'(ha) "reconnaissance operations" means any operations undertaken for
preliminary prospecting of a mineral through regional, aerial, geophysical orgeochemical surveys and geological mapping, and include pitting, trenching,drilling and sub-surface excavation;'.
3. In section 4 of the principal Act, in sub-section ( 1), after the words "prospecting
licence", the words "or of a exploration licence" shall be inserted.
4. In section 4A of the principal Act,—
(i) for the marginal heading, the following marginal heading shall be substituted,
namely:—
"Termination of prospecting licences, exploration licences or mining
leases.";
(ii) in sub-section ( 1), for the words "prospecting licence", at both the places
where they occur, the words "prospecting licence or exploration licence" shall besubstituted;
(iii) in sub-section ( 3), after the words "prospecting licence", the words "or
exploration licence" shall be inserted.
5. In section 5 of the principal Act, for the marginal heading, the following marginal
heading shall be substituted, namely:—
"Restrictions on the grant of mineral concession.".
6. In section 6 of the principal Act,—
(a) for the marginal heading, the following marginal heading shall be substituted,
namely:—
"Maximum area for which mineral concession may be granted.";
(b) in sub-section ( 1),—
(i) after clause ( aa), the following clause shall be inserted, namely:—
"(ab) one or more exploration licences covering a total area of more
than five thousand square kilometres:
Provided that the area granted under a single exploration licence
shall not exceed one thousand square kilometres;";
(ii) in clause ( c), for the words "reconnaissance permit, mining lease or
prospecting licence", the words "mineral concession" shall be substituted.
7. In Chapter III of the principal Act, for Chapter heading, the following Chapter
heading shall be substituted, namely:—
"P
ROCEDURE  FOR OBTAINING  MINERAL  CONCESSION  IN RESPECT  OF LAND  IN WHICH  THE
MINERALS  VEST IN THE GOVERNMENT ".Amendment
of section 3.
Amendment
of section 4.
Amendment
of section 5.
Amendment
of section 6.
Substitution
of Chapterheading ofChapter III.67 of 1957.
Amendment
of section 4A.
SEC. 1] THE GAZETTE OF INDIA EXTRAORDINARY 3
8. In section 10 of the principal Act,—
(i) for the marginal heading, the following marginal heading shall be substituted,
namely:—
"Application for mineral concession.";
(ii) in sub-section ( 4), in clause ( a), for the words, figures and letters "sections
10B, 11, 11A or the rules made under section 11B", the words, figures and letters"sections 10B, 10BA, 11, 11A, 11B or 11D" shall be substituted.
9. After section 10B of the principal Act, the following section shall be inserted,
namely:—
"10BA. ( 1) The provisions of this section shall not apply to—
(a) the areas covered under section 17A;
(b) the minerals specified in Part A of the First Schedule;
(c) the minerals specified in Part B of the First Schedule where the grade of
atomic mineral is equal to or greater than such threshold value as may be notifiedby the Central Government from time to time;
(d) any land in respect of which the minerals do not vest in the Government.
(2) Notwithstanding anything contained in sections 10B and 11, an exploration
licence may be granted in any area by the State Government for the purpose ofundertaking reconnaissance or prospecting operations or both in respect of any mineralspecified in the Seventh Schedule.
(3) The Central Government may , by notification in the Official Gazette, and for
reasons to be recorded in writing, amend the Seventh Schedule so as to modify theentries therein with effect from such date as may be specified in the said notification.
(4) The State Government shall, after obtaining the previous approval of the
Central Government, and in such manner as may be prescribed by the CentralGovernment, notify the areas in which exploration licence shall be granted, subject tosuch terms and conditions as may be specified in the notification.
(5) The Central Government may require the State Government to notify the area
for grant of exploration licence within such period as may be fixed in consultation withthe State Government, and in case the State Government does not notify the areawithin such period, the Central Government may, after the expiry of the period so fixed,notify the area for grant of exploration licence.
(6) The State Government shall, for the purpose of granting exploration licence
through auction by method of competitive bidding, including e-auction, select anapplicant who fulfils the eligibility conditions as specified in this Act and grantexploration licence to such applicant.
 (7) Where—
(a) the State Government has not successfully completed auction for the
grant of exploration licence; or
(b) after completion of auction, the exploration licence or letter of intent for
grant of exploration licence has been terminated or lapsed for any reasonwhatsoever,
the Central Government may require the State Government to conduct and complete
the auction or re-auction process, as the case may be, within such period as may befixed in consultation with the State Government, and in cases where such auction orre-auction process is not completed within such period, the Central Government may,after the expiry of the period so fixed, conduct auction for the grant of explorationlicence for such area:Amendmentof section 10.
Insertion of
new section10BA.
Grant of
explorationlicence formineralsspecified inSeventhSchedulethroughauction.
4 THE GAZETTE OF INDIA EXTRAORDINARY [P ART II—
Provided that upon successful completion of the auction, the Central Government
shall intimate the details of the preferred bidder in the auction to the State Governmentand the State Government shall grant exploration licence for such area to such preferredbidder in such manner as may be prescribed by the Central Government.
(8) The holder of exploration licence shall be entitled to a share of applicable
amount quoted in the auction of mining leases payable by the lessee to the StateGovernment in respect of the area granted in mining lease pursuant to the prospectingoperations undertaken by the holder of such exploration licence:
Provided that the share in applicable amount payable to the holder of exploration
licence by the lessee of such area shall be allowed only in respect of the mineralsspecified in the Seventh Schedule.
(9) The Central Government shall by rules provide for the manner of conducting
auction for grant of exploration licence, including its terms and conditions, the biddingparameters for selection, share payable to the holder of exploration licence from out ofthe applicable amount quoted in auction of mining leases payable by the lessee ofsuch area, the period for such payment and such other conditions as may be necessary.
(10) Notwithstanding anything contained in section 7,—
(a) the exploration licence shall be granted for a period of five years from
the date of execution of the exploration licence;
(b) if, after three years from the date of execution of exploration licence,
but before the date of its expiry, the holder of the exploration licence makes anapplication for the extension of the period of that licence, the State Governmentmay, on being satisfied that within the period of five years, it shall not be possiblefor the holder of such licence to complete the reconnaissance or prospectingoperations for reasons beyond his control, extend the said period to a furtherperiod not exceeding two years.
(11) After three years from the date of execution of the exploration licence, the
holder of such licence may retain an area not exceeding twenty-five per cent. of thetotal area covered under that licence for the purpose of continuing reconnaissance orprospecting operations and shall surrender the remaining area after submitting a reportto the State Government stating the reasons for retention of the area proposed to beretained by him and the boundaries of that area.
(12) The holder of the exploration licence shall, within three months of the
completion of the operations for which licence has been granted, or of the date ofexpiry of the exploration licence, whichever is earlier, submit a geological report to theState Government explaining the result of the reconnaissance and prospectingoperations, in such manner as may be prescribed.
(13) If the holder of the exploration licence fails to complete the reconnaissance
and prospecting operations before expiry of the exploration licence, or fails to submitthe geological report within the period specified in sub-section ( 12), the State
Government may take such action as it deems fit, including imposition of penalty.
(14) Within six months from the date of receipt of the geological report from the
holder of the exploration licence, the Central Government or the State Governmentshall initiate the auction process for grant of one or more separate mining leases undersection 10B or section 11 or section 11D, as the case may be, in respect of the areawhere existence of mineral content is established and shall select the preferred bidderfor grant of such mining leases within one year from the date of receipt of
the geologicalreport:
Provided that in case the preferred bidder is not selected within the period so
specified, the State Government shall pay to the person who was the holder of explorationlicence such amount, and in such manner, as may be prescribed.".
SEC. 1] THE GAZETTE OF INDIA EXTRAORDINARY 5
10.  After section 11C, the following section shall be inserted, namely:—
"11D. ( 1) Notwithstanding anything contained in this Act, the Central Government
shall, for the purpose of granting mining lease or composite licence in any area inrespect of any mineral specified in the Part D of the First Schedule, select, throughauction by method of competitive bidding, including e-auction, a preferred bidder whofulfils the eligibility conditions as specified in section 5, on such terms and conditions,and in such manner, as may be prescribed.
(2) Upon successful completion of the auction, the Central Government shall
intimate the details of the preferred bidder in the auction to the State Government andthe State Government shall grant mining lease or composite licence for such area, tosuch preferred bidder, in such manner, as may be prescribed by the Central Government.
(3) The royalty, dead rent, applicable amount quoted in the auction and any
other statutory payment in relation to the mining lease or composite licence auctionedby the Central Government shall accrue to the State Government or concernedauthorities, as the case may be, as if the auction has been conducted by the StateGovernment.".
11. In section 12 of the principal Act,—
(a) for the marginal heading, the following marginal heading shall be substituted,
namely:—
"Registers of mineral concession.";
(b) in sub-section ( 1),—
(i) in clause ( e), the word "and" shall be omitted;
(ii) after clause ( f), the following clauses shall be inserted, namely:—
"(g) a register of applications for exploration licences; and
(h) a register of exploration licences,".
12. In section 12A of the principal Act,—
(i) after the words "composite licence", wherever they occur, the words "or
exploration licence" shall be inserted;
(ii) in sub-section ( 4), in the proviso, for the words "or of a composite licence",
the words "or composite licence" shall be substituted.
13. In Chapter IV of the principal Act, for Chapter heading, the following Chapter
heading shall be substituted, namely:—
"R
ULES FOR REGULA TING  THE GRANT  OF MINERAL  CONCESSIONS ".
14. In section 13 of the principal Act, in sub-section ( 2),—
(i) clause ( ac) shall be omitted;
(ii) in clause ( qqg), for the words, figures and letters "mining lease or composite
licence under section 10B, 11, 11A, 11B", the words, figures and letters "mineralconcession under section 10B, 10BA, 11, 11A, 11B, 11D" shall be substituted;
(iii) after clause ( v), the following clauses shall be inserted, namely:—
"(va) the manner of notifying the areas for grant of exploration licence
under sub-section ( 4) of section 10BA;
(vb) the manner of granting exploration licence to the preferred bidder
under the proviso to sub-section ( 7) of section 10BA;Insertion of
new section11D.
Central
Governmentto conductauction forgrant ofmining leaseor compositelicence inrespect ofmineralsspecified inPart D ofFirstSchedule.
Amendment
of section 12.
Amendment
of section12A.
Substitution
of Chapterheading ofChapter IV.
Amendment
of section 13.
6 THE GAZETTE OF INDIA EXTRAORDINARY [P ART II—
(vc) the manner of conducting auction for grant of exploration licence, the
terms and conditions thereof, the bidding parameters for selection, the sharepayable to the holder, the period for payment and other conditions undersub-section ( 9) of section 10BA;
(vd) the manner of submitting geological report under sub-section ( 12) of
section 10BA;
(ve) the amount to be paid and the manner of payment under the proviso
to sub-section ( 14) of section 10BA;";
(iv) after clause ( x), the following clauses shall be inserted, namely:—
"(xa) the terms and conditions and the manner of selecting a preferred
bidder under sub-section ( 1) of section 11D;
(xb) the manner of granting a mining lease or composite licence to a
preferred bidder under sub-section ( 2) of section 11D;".
15. In section 17A of the principal Act, in sub-sections ( 1), (1A) and ( 2), after the words
"prospecting licence", the words "or exploration licence" shall be inserted.
16. In section 18A of the principal Act, in sub-section ( 1), after the words "prospecting
licence", at both the places where they occur, the words "or exploration licence" shall beinserted.
17. In section 19 of the principal Act, for the marginal heading, the following marginal
heading shall be substituted, namely:—
"Mineral concession to be void if in contravention of Act.".
18. In section 21 of the principal Act, in the Explanation , after the words "composite
licence", the words ", exploration licence" shall be inserted.
19. In section 24A of the principal Act, for the marginal heading, the following marginal
heading shall be substituted, namely:—
"Rights and liabilities of a holder of mineral concession.".
20.  In the principal Act, in the First Schedule,—
(i) after the figures and letter  “11C”, the figures and letter  “11D” shall be inserted;
(ii) for Part B, the following Part shall be substituted, namely:—
"P ART B
Atomic minerals
1. Minerals of the "rare earths" group containing Uranium and Thorium.
2. Phosphorites and other phosphatic ores containing Uranium.
3. Pitchblende and other Uranium ores.
4. Uraniferous allanite, monazite and other thorium minerals.
5. Uranium bearing tailings left over from ores after extraction of copper
and gold, ilmenite and other titanium ores.
6. Beach sand minerals, that is, economic heavy minerals found in the teri
or beach sands, which include ilmenite, rutile, leucoxene, garnet,monazite, zircon and sillimanite.";Amendmentof section17A.
Amendment
of section18A.
Amendment
of section 19.
Amendment
of section 21.
Amendment
of section24A.
Amendment
of FirstSchedule.
SEC. 1] THE GAZETTE OF INDIA EXTRAORDINARY 7
 (iii) after Part C, the following Part shall be inserted, namely:—
"P ART D
Critical and Strategic Minerals
1. Beryl and other beryllium bearing minerals.2. Cadmium bearing minerals.3. Cobalt bearing minerals.4. Gallium bearing minerals.5. Glauconite.6. Graphite.7. Indium bearing minerals.8. Lithium bearing minerals.9. Molybdenum bearing minerals.
10. Nickel bearing minerals.11. Niobium bearing minerals.12. Phosphate (without uranium).13. Platinum group of elements bearing minerals.14. Potash.15. Minerals of the "rare earths" group not containing Uranium and Thorium.
16. Rhenium bearing minerals.
17. Selenium bearing minerals.18. Tantalum bearing minerals.19. Tellurium bearing minerals.20. Tin bearing minerals.21. Titanium bearing minerals and ores (ilmenite, rutile and leucoxene).22. Tungsten bearing minerals.23. Vanadium bearing minerals.24. Zirconium bearing minerals and ores including zircon.".
21. In the principal Act, after Sixth Schedule, the following shall be inserted, namely:—
"THE SEVENTH SCHEDULE
[ See sections 3 ( aaa), 10BA( 2) and 10BA( 3)]
Minerals
1. Apatite.2. Beryl and other beryllium bearing minerals.3. Cadmium bearing minerals.4.  Cobalt bearing minerals.5. Copper bearing minerals.
Insertion of
new SeventhSchedule.
8 THE GAZETTE OF INDIA EXTRAORDINARY [P ART II—
6. Diamond.
7. Gold.8. Graphite.9. Indium bearing minerals.10. Lead bearing minerals.11.  Lithium bearing minerals.12. Molybdenum bearing minerals.13. Niobium bearing minerals.14. Nickel bearing minerals.15. Potash.16. Platinum group of elements bearing minerals.17. Minerals of 'rare earths' group.18. Rhenium bearing minerals.19. Rock Phosphate.20.  Selenium.21. Silver.22. Tantalum bearing minerals.23. Tellurium bearing minerals.24. Tin bearing minerals.25. Titanium bearing minerals and ores (ilmenite, rutile and leucoxene).26. Tungsten bearing minerals.27. Vanadium bearing minerals.28. Zinc bearing minerals.29. Zirconium bearing minerals and ores including zircon.".
————
DR. REETA VASISHTA,
Secretary to the Govt. of India.
————
CORRIGENDA
THE BIOLOGICAL DIVERSITY (AMENDMENT) ACT , 2023
No. 10
OF 2023
In the BIOLOGICAL DIVERSITY (AMENDMENT) ACT, 2023 (10 OF 2023), as
published in the Gazette of India, Extraordinary, Part II Section, 1, dated the 3rd August, 2023,Issue No. 13,—
(i) in page 2, line 41,  for ‘‘refferred’’,  read  ‘‘referred’’;
(ii) in page 4, line 17,  for ‘‘Biodivesity’’,  read  ‘‘Biodiversity’’;
(iii) in page 5, line 16,  for ‘‘Pachayati’’,  read  ‘‘Panchayati’’;
(iv) in page 8, line 3,  for ‘‘Commitee’’,  read  ‘‘Committee’’;
SEC. 1] THE GAZETTE OF INDIA EXTRAORDINARY 9
MGIPMRND—273GI(S3)—09-08-2023.UPLOADED BY THE MANAGER, GOVERNMENT OF INDIA PRESS, MINTO ROAD,  NEW DELHI–110002
AND PUBLISHED BY THE CONTROLLER OF  PUBLICATIONS, DELHI–110054.(v) in page 8, line 22,  for ‘‘affiairs’’,  read  ‘‘affairs’’;
(vi) in page 8, line 31,  for ‘‘sustainble’’,  read  ‘‘sustainable’’;
(vii) in page 8, line 39,  for ‘‘princiapal’’,  read  ‘‘principal’’;
(viii) in page 11, line 25,  for ‘‘as prescribed’’,  read  ‘‘as may be prescribed’’;
(ix) in page 12, line 10,  for ‘‘veriety’’,  read  ‘‘variety’’;
(x) in page 12, line 17,  for ‘‘veriety’’,  read  ‘‘variety’’;
(xi) in page 12, line 20,  for ‘‘veriety’’,  read  ‘‘variety’’;
(xii) in page 12, line 26,  for ‘‘substiututed’’,  read  ‘‘substituted’’;
(xiii) in page 13, line 1,  for ‘‘prinicpal’’,  read  ‘‘principal’’;
(xiv) in page 13, line 11,  for ‘‘princiapl’’,  read  ‘‘principal’’;
(xv) in page 13, line 34,  for ‘‘penalities’’,  read  ‘‘penalties’’;
(xvi) in page 14, line 3,  for ‘‘accordance the’’,  read  ‘‘accordance with the’’.

page count: 9
'''
