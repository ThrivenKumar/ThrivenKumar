class numbers{
  public static void main(String args[]){
    int a=0,b=0,c=0,d=0,i=0,j=0,k=0,l=0,count1=0,count2=0,z=1;
    for(i=0;i<10;i++){
      a=i;
      for(j=0;j<10;j++){
        b=j;
        for(k=0;k<10;k++){
          c=k;
          for(l=0;l<10;l++){
            d=l;
            count1=a+b+c+d;
            count2=count1%10;
            count2+=count1/10;
            if(count2==5||count2==6){
              System.out.print(a+" "+b+" "+c+" "+d+"    ");
              if(z%7==0)
                System.out.println();
              z++;
            }
          }
        }
      }
    }
  }
}
