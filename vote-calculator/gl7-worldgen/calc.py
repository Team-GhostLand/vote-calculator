import sys;

class ParseResult:
    tect_or_cont: str
    preffered_range: str
    scores = [0,0,0,0,0,0,0,0,0,0,0,0,0] #1-12 --> BOP-Envi  ;  0 --> dummy   #Why can't I just do scores: int[12]? I dunno! Pylance had no problems with it, but Python wouldn't accept it.

#yandere-ahh code (if this wasn't a one-off thing, I'd probably give enough fucks to read IDs from a file, or something - but it IS a one-off, so I don't care)
def textToModID(text: str):
    #Either Python doesn't have Switch-statements, or I don't have the snippet for it. And I'm too lazy to check.
    if text=="Biomes o' Plenty":
        return 1;
    if text=="Oh the biomes we've gone (you'll go)":
        return 2;
    if text=="Terralith (nie psuje Create - patrz: mythbusting)":
        return 3;
    if text=="Regions Unexplored":
        return 4;
    if text=="Terrestria":
        return 5;
    if text=="Traverse":
        return 6;
    if text=="Biome Makeover":
        return 7;
    if text=="Williams Wythers Overhauled Overworld":
        return 8;
    if text=="Williams Wythers Expanded Ecosphere":
        return 9;
    if text=="Promenade":
        return 10;
    if text=="Atmospheric":
        return 11;
    if text=="Environmental":
        return 12;
    return 0;

def parseLine(line: str):
    print("\n\nParsing line: ", line);
    anwsers = line.split("\t");
    results = ParseResult();
    score_parse_start = 5
    score_parse_end = 10;
    results.scores = [0,0,0,0,0,0,0,0,0,0,0,0,0] #Ig I really don't understand how python classes work??? Cuz it SHOULD „reset” in a normal goddamn language, every time I make a new instance. You know, it should actually be a new one. But here it just... Isn't. It's like the class wasn't even there and this thing was a global object. Is calling ClassName() not how I create a new instance? But doing new ClassName() doesn't work, either??? How tf do I get a new instance, instead of just referencing the same one, over and over again???? Why did I pick Python again?
     
    #Date:0
    #Name:1
    #Accept:2
    results.tect_or_cont = anwsers[3];
    #Accept:4
    results.preffered_range = anwsers[score_parse_end]; #ie. 10
    
    for index in range(score_parse_start, score_parse_end):
        max_score = 5; # <-- COINCIDENCE THAT THIS IS ALSO FIVE
        score = max_score-(index-score_parse_start); #5,6,7,8,9 --> 0,1,2,3,4 --> 5,4,3,2,1
        results.scores[textToModID(anwsers[index])] = score;
        print("Przyznawanie ", anwsers[index], ":", textToModID(anwsers[index]), " punktów: ", score, sep="");

    return results;

def printSkips(skips: int, total: int, valid: int):
    print("  * ", skips,"/",total, " (",(skips/total*100),"%) pominiętych ---> Zostaje ", valid, sep="");

def printVotes(votes: int, total: int, valid: int, vote_for: str):
    print("  * ", votes,"/",valid, " (",(votes/total*100),"% wszystkich i ",(votes/valid*100),"% ważnych) na: ", vote_for, sep="");

def printTerrain(votes: int, valid: int, vote_for: str):
    percentage = votes/valid*100
    status = "[#ERR!]"
    if percentage > 50 and percentage <= 100:
        status = "ZOSTAJE!";
    elif percentage < 50 and percentage >= 0:
        status = "ODPADA!";
    elif percentage == 50:
        status = "przechodzi do drugiej tury.";
    print("  * ", percentage,"% (", votes, "/", valid, ") ważnych głosów zawierało w sobie ", vote_for, "  ----> ", vote_for, " ", status, " (*subject to change)", sep="");



if len(sys.argv) < 2:
    print("Please specify filepath!");
    exit(1);
elif len(sys.argv) > 2:
    print("Too many arguments! One expected.");
    exit(1);

#File
file = open(sys.argv[1], "r");
lines = file.readlines();
cast_votes = 0;
#Terrain
tect = 0;
cont = 0;
tect_only = 0;
cont_only = 0;
both = 0;
none = 0;
skipped_terrain = 0;
#Biomes
score_BOP = 0;
score_BYG = 0;
score_Terralith = 0;
score_RUx = 0;
score_Terrestria = 0;
score_Trav = 0;
score_BMO = 0;
score_WWOO = 0;
score_WWEE = 0;
score_Prom = 0;
score_Atmo = 0;
score_Envi = 0;
#Size
under_2k = 0;
betwen_2k_and_3k = 0;
betwen_4k_and_5k = 0;
betwen_7k_and_8k = 0;
betwen_9k_and_10k = 0;
above_10k = 0;
skipped_size = 0;

isFirst = True;
for line in lines:
    if isFirst:
        isFirst = False;
        print("Skipping header...");
        continue;
    parsed = parseLine(line);
    cast_votes += 1;

    score_BOP += parsed.scores[1];
    score_BYG += parsed.scores[2];
    score_Terralith += parsed.scores[3];
    score_RUx += parsed.scores[4];
    score_Terrestria += parsed.scores[5];
    score_Trav += parsed.scores[6];
    score_BMO += parsed.scores[7];
    score_WWOO += parsed.scores[8];
    score_WWEE += parsed.scores[9];
    score_Prom += parsed.scores[10];
    score_Atmo += parsed.scores[11];
    score_Envi += parsed.scores[12];

    if parsed.tect_or_cont == "oba":
        tect += 1; #Either Python doesn't support n++, or Pylance is stupid.
        cont += 1;
        both += 1;
    elif parsed.tect_or_cont == "Tectonic":
        tect += 1;
        tect_only += 1;
    elif parsed.tect_or_cont == "Continents":
        cont += 1;
        cont_only += 1;
    elif parsed.tect_or_cont == "żaden":
        none += 1;
    else:
        skipped_terrain += 1;
    
    if parsed.preffered_range == "Mniej niż 2k od spawnu":
        under_2k += 1;
    elif parsed.preffered_range == "2-3k od spawnu":
        betwen_2k_and_3k += 1;
    elif parsed.preffered_range == "4-5k od spawnu":
        betwen_4k_and_5k += 1;
    elif parsed.preffered_range == "7-8k od spawnu":
        betwen_7k_and_8k += 1;
    elif parsed.preffered_range == "9-10k od spawnu":
        betwen_9k_and_10k += 1;
    elif parsed.preffered_range == "więcej":
        above_10k += 1;
    else:
        skipped_size += 1;

print("\n\n\n---------- WYNIKI: ----------");
print("> TEREN:");
cast_terrain = none+both+tect_only+cont_only;
printSkips(skipped_terrain, cast_votes, cast_terrain);
printVotes(both, cast_votes, cast_terrain, "Both");
printVotes(none, cast_votes, cast_terrain, "Żaden");
printVotes(tect_only, cast_votes, cast_terrain, "Tylko Tectonic");
printVotes(cont_only, cast_votes, cast_terrain, "Tylko Continents");
printTerrain(tect, cast_terrain, "Tectonic");
printTerrain(cont, cast_terrain, "Continents");
print("> RANKING:");
print("  * BOP:", score_BOP, "punkt(y/-ów)");
print("  * BYG:", score_BYG, "punkt(y/-ów)");
print("  * Terralith:", score_Terralith, "punkt(y/-ów)");
print("  * RUx:", score_RUx, "punkt(y/-ów)");
print("  * Terrestria:", score_Terrestria, "punkt(y/-ów)");
print("  * Trav:", score_Trav, "punkt(y/-ów)");
print("  * BMO:", score_BMO, "punkt(y/-ów)");
print("  * WWOO:", score_WWOO, "punkt(y/-ów)");
print("  * WWEE:", score_WWEE, "punkt(y/-ów)");
print("  * Prom:", score_Prom, "punkt(y/-ów)");
print("  * Atmo:", score_Atmo, "punkt(y/-ów)");
print("  * Envi:", score_Envi, "punkt(y/-ów)");
print("> ROZMIAR: ");
cast_size = cast_votes-skipped_size;
printSkips(skipped_size, cast_votes, cast_size);
printVotes(under_2k, cast_votes, cast_size, "<2k");
printVotes(betwen_2k_and_3k, cast_votes, cast_size, "2-3k");
printVotes(betwen_4k_and_5k, cast_votes, cast_size, "4-5k");
printVotes(betwen_7k_and_8k, cast_votes, cast_size, "7-8k");
printVotes(betwen_9k_and_10k, cast_votes, cast_size, "9-10k");
printVotes(above_10k, cast_votes, cast_size, ">10k");