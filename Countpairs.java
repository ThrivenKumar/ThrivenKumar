import java.util.*;
import java.io.*;
class Countpairs{
  public static void main(String[] args){
    int i,j=0,temp,count=0;
    int ArrayLength=Integer.parseInt(args[0]);
    int k=Integer.parseInt(args[1]);
    int[] NumberArray=new int[ArrayLength+2];
    for(i=2;i<ArrayLength+2;i++){
      j++;
      NumberArray[j]=Integer.parseInt(args[i]);
    }
    for (i = 1; i <= ArrayLength; i++)
    {
      int min_idx = i;
      for (j = i+1; j <=ArrayLength; j++)
        if (NumberArray[j] < NumberArray[min_idx])
          min_idx = j;
      temp = NumberArray[min_idx];
      NumberArray[min_idx] = NumberArray[i];
      NumberArray[i] = temp;
    }
    NumberArray[0]=NumberArray[1]-4;
    NumberArray[i]=NumberArray[i-1]+4;
    for(i=1;i<=ArrayLength;i++){
      if(NumberArray[i]-3<=NumberArray[i-1]||NumberArray[i]+3>=NumberArray[i+1]){
        count++;
      }
    }
    System.out.println("No of happy elements: "+count);
  }
}
