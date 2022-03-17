import java.util.*;
class solution {
    public static List<Integer> findSubstring(String s, String[] words) {
        int len=words[0].length();
        int index=0;
        ArrayList<Integer> indices=new ArrayList<Integer>();
        int j1=0;
        for(String key:words){
            s=s.replaceAll(key, " "+j1+" ");
            j1++;
        }
        String a[]=s.trim().split("  *");
        ArrayList<String> temp=new ArrayList<String>();
        for (int i=0;i<a.length;i++){
            for (int j=i;j<a.length;j++){
                if ( !temp.contains(a[j]) && isNumeric(a[j]) ){
                    temp.add(a[j]);
                }
                else{
                    break;
                } 
            }
            if(i>0){
                if(a[i-1].length()==1){
                    index+=len;
                }
                else{
                    index+=a[i-1].length();
                }
            }
            if(temp.size()==words.length){
                indices.add(index);
            }
            temp.clear();
        }
        return indices; 
        
    }
    public static boolean isNumeric(String str) { 
        try {  
            Integer.parseInt(str);
            return true;
        } 
        catch(NumberFormatException e){  
            return false;  
        }  
    }

    public static void main(String args[]){
        String arr[]=new String[]{"foo","bar"};
        System.out.println(findSubstring("barfoothefoobarman",arr));
    }
}