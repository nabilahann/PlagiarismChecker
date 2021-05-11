from BoyerMoore import bmMatch

def tingkatPlagiarisme(doc1, final_list) : 
    lenArr = len(doc1)
    #print(lenArr)
    lenFinal = len(final_list)
    #print(lenFinal)
    hasil = (lenFinal/lenArr) * 100
    return hasil

def PlagiarismChecker(namafile1, namafile2):
    # Read file
    file1=open(namafile1,"r")
    text1=file1.readlines()

    file2=open(namafile2,"r")
    text2=file2.readlines()

    # Convert list to string 
    str1=''.join(text1)
    str2=''.join(text2)

    # Split the string
    sent_text1=str1.split('.')
    sent_text2=str2.split('.')

    sent_text1.remove("")
    sent_text2.remove("")
    # print(sent_text1)
    # print(sent_text2)

    # Create a for loop that compares two lists
    final_list=[]
    for z in sent_text1:
        for y in sent_text2:
            if (bmMatch(y,z) != -1) :
                final_list.append(z)

    # Print result
    print("Tingkat Plagiarisme : ", tingkatPlagiarisme(sent_text1, final_list),"%")

    print("Analisis Dokumen : ")
    for z in sent_text1:
        if (z in final_list) :
            bolded_string = "\033[1m" + z + "\033[0m"
            print(bolded_string)
        else :
            print(z)

    

# Driver program to test above function
def main():
    namafile1 = input("Masukkan nama file 1 : ")
    namafile2 = input("Masukkan nama file 2 : ")

    PlagiarismChecker(namafile1, namafile2)

if __name__ == '__main__':
    main()