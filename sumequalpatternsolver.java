
import java.util.*;
public class sumequalpatternsolver{
    ArrayList<Integer> numlist=new ArrayList<Integer>(25);
    int arr[][]=new int[5][5];

    sumequalpatternsolver(){
        for (int i=0;i<5;i++){
            for (int j=0;j<5;j++){
                arr[i][j]=j;
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }
    
    public int backtracker(int row, int col){
        int val=-1;
        for (int i=1;i<26;i++){
            if(!numlist.contains(i)){
                a[row][col]=i;
            }
            if(row<5 && col<5){
                val=backtracker(row,col+1);
            }
            else if(row==4 && col>4){
                System.out.println("Terminating because row is "+row);
                return 10;
            }
            else if(row<4 && col>4){
                col=0;
                row++;
                val=backtracker(row,col);
            }
        }
        return 0;
    }

    public void printMatrix(){
        for (int i=0;i<5;i++){
            for (int j=0;j<5;j++){
                arr[i][j]=j;
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }

    public int count(int row, int col){
        boolean booli=false;
        int temp=0;
        if(row==4 && col<4){
            for (int i=0;i<5;i++){
                temp+=arr[i][col];
            }
            if(temp==65){
                return 1;
            }
            System.out.println("Backtracking at Row: "+ row + " Col: "+ col+ " "+ arr[row][col]);
            printMatrix();
            return 0;
        }
        else if(row<4 && col==4){
            for (int i=0;i<5;i++){
                temp+=arr[row][i];
            }
            if(temp==65){
                return 1;
            }
            System.out.println("Backtracking at Row: "+ row + " Col: "+ col+ " "+ arr[row][col]);
            printMatrix();
            return 0;
        }
        else if (row==4&&col==4){
            for (int i=0;i<5;i++){
                temp+=arr[i][col];
            }
            if(temp!=65){
            System.out.println("Backtracking at Row: "+ row + " Col: "+ col+ " "+ arr[row][col]);
            printMatrix();
                return 0;
            }
            temp=0;
            for (int i=0;i<5;i++){
                temp+=arr[row][i];
            }
            if(temp!=65){
                System.out.println("Backtracking at Row: "+ row + " Col: "+ col+ " "+ arr[row][col]);
                printMatrix();
                return 0;
            }
            return 1;
        }
        else{
            for (int i=0;i<5;i++){
                temp+=arr[i][col];
            }
            if(temp>=65){
            System.out.println("Backtracking at Row: "+ row + " Col: "+ col+ " "+ arr[row][col]);
            printMatrix();
                return 0;
            }
            temp=0;
            for (int i=0;i<5;i++){
                temp+=arr[row][i];
            }
            if(temp>=65){
            System.out.println("Backtracking at Row: "+ row + " Col: "+ col+ " "+ arr[row][col]);
            printMatrix();
                return 0;
            }
            return 1;
        }
    }
    public static void main(String args[]){
        sumequalpatternsolver seps=new sumequalpatternsolver();
    }
}