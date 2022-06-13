class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        ransomDict, magazineDict = {}

        for let in ransomNote:

            if let in ransomDict:
                ransomDict[let]+=1
            else:
                ransomDict[let]=1

        
        for let in magazine:

            if let in magazineDict:
                magazineDict[let]+=1
            else:
                magazineDict[let]=1

        for key in ransomDict:
            ##for every letter required in ransom

            if key in magazineDict:

                if ransomDict[key]>magazineDict[key]:
                    ##not enough letters in magazine, return false
                    return False
            else:
                ##not in magazine, cant make ransom
                return False
        return True