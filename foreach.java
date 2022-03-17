import java.util.*;
class foreach {
    public static void main(String args[]){
        int a[]=new int[3];
        a[0]=10;
        a[1]=20;
        a[2]=30;
        // for(int i:a){
        //     System.out.println(i);
        // }
        ArrayList<Integer> arr=new ArrayList<Integer>();
        arr.add(3);
        arr.add(2);
        arr.add(1);
        arr.add(4);
        arr.add(2,8);
        // Collections.sort(arr);
        arr.remove();
        for (int i:arr){
            System.out.println(i);
        }
        
    }
}