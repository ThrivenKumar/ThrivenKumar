public class arrayList {
    public static void main(String args[]){
        // int a=681;
        // long l=7916L;
        // //String b=Long.toString(a+l);
        // char d=(char)a;
        // System.out.println(d);
        // String s="  ";
        // System.out.println(s.isEmpty());
        String s="a";
        StringBuilder temp=new StringBuilder(s);
        temp.reverse();
        int maxlength=0,sublen;
        int len=s.length();
        int j,k,temp2;
        int start=0;
        for (int i=0; i<len; i++){
            j=i;
            k=len-1;
            temp2=k;
            sublen=0;
            while(i<=k){
                if (s.charAt(j)==s.charAt(k)){ 
                    j++;
                    sublen++;
                    k--;
                }
                else{
                    j=i;
                    sublen=0;
                    k=--temp2;
                }
            }
            if(maxlength<sublen){
                maxlength=sublen;
                start=i;
                System.out.println(sublen + " "+ start);
            }
        }
        if(maxlength>0){
            System.out.println(s.substring(start,start+maxlength));
        }

    }
}
