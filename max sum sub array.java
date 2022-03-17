import java.io.*;
import java.util.*;
class UserMainCode{
    static int majority(int input1,int[] input2){
        int i,j,k=2,sum=0,result,max;
        max=input2[0];
        for(i=0;i<input1;i++){
            if (max<input2[i]){
                max=input2[i];
            }
        }
        result=max;
        while(k<=input1){
            for (i=0;i<=input1-k;i++){
                sum=0;
                for(j=i;j<k+i;j++){
                    System.out.println(i+ " "+ j);
                    sum+=input2[j];
                }
                System.out.println(sum);
            }
            if(sum>result){
                result=sum;
            }
            k++;
        }
        return result;
    }
    public static void main(String args[]){
        int[] a={1,2,3,4,5};
        int v=majority(a.length, a);
        System.out.println(v);
    }
}