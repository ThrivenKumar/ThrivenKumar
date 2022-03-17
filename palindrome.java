import java.util.*;
class palindrome{
    void findPalindrome(String testcase){
        int i=0,k,l,j=0;
        boolean booli=true;
        while(i<testcase.length()){
            j=i+2;
            while(j<testcase.length()){
                l=j;
                for(k=i;k<=j;k++){
                    if(testcase.charAt(k)!=testcase.charAt(l)){
                        booli=false;
                    }
                    l--;
                }
                j=j+2;
            }
            i++;
        }
        if(booli==true){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
    }
    public static void main(String args[]){
        int i;
        palindrome p=new palindrome();
        Scanner sc=new Scanner(System.in);
        int len=sc.nextInt();
        String a[]=new String[len];
        for (i=0;i<len;i++){
            a[i]=sc.next();
        }
        for(i=0;i<len;i++)
            p.findPalindrome(a[i]);
    }
}