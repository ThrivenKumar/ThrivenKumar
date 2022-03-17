import java.util.*;
import java.io.*;
class cars24{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int nodes,i,j,k;
        nodes=s.nextInt();
        int[][] edges=new int[nodes+1][nodes+1];
        for(i=1;i<=nodes;i++){
            for(j=1;j<=nodes;j++)
                edges[i][j]=0;
        }
        int color[]=new int[nodes+1];
        int a,b;
        color[0]=1;
        for(i=1;i<=nodes;i++){
            b=s.nextInt();
            color[i]=b;
        }
        for(i=0;i<nodes-1;i++){
            a=s.nextInt();
            b=s.nextInt();
            edges[a][b]=1;
            edges[b][a]=1;
        }
        int flag=1,index;
        j=1;
        int[] newcolors=new int[nodes];
        newcolors[0]=1;
        index=1;
        for(i=2;i<=nodes;i++){
            if(color[i]==0&&(color[i-1]==1||color[i-1]==0)){
                index=i;
                newcolors[j]=i;
                flag=1;
                j++;
            }
            else if(color[i]==1&&color[i-1]==0){
                index=i;
                newcolors[j]=i;
                flag=1;
                j++;
            }
            else{
                for(k=1;k<=nodes;k++)
                    edges[index][k]+=edges[index+flag][k];
                for(k=1;k<=nodes;k++)
                    edges[k][index]+=edges[k][index+flag];
                flag+=1;
            }
        }
        System.out.println();
        for(i=0;i<newcolors.length;i++)
            System.out.print(newcolors[i]+" ");
        System.out.println();
        for(i=1;i<nodes+1;i++){
            for(j=1;j<nodes+1;j++){
                System.out.print(edges[i][j]+" ");
            }
            System.out.println();
        }
        int count=0,count2,n;
        for(i=1;i<newcolors.length+1;i++){
            count2=-1;
            n=0;
            if(color[newcolors[i-1]]==1){
                for(j=1;j<newcolors.length+1;j++){
                    if(edges[i][j]>=1&&color[newcolors[j-1]]==0){
                        count2+=1;
                    }
                }
                System.out.println(count2+" ");
                if(count2>0)
                    n=(count2*(count2+1))/2;
                count+=n;
            }
        }
        System.out.println("No of distinct pairs: "+count);
    }
}