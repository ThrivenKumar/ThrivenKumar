import java.util.*;
class Heap{
    ArrayList<Integer> heapArray;
    Heap(){
        this.heapArray=new ArrayList<Integer>();
    }
    public void insertElement(int num){
        heapArray.add(num);
        int lastIndex=heapArray.size()-1;
        boolean bool=true;
        int temp;
        while (bool){
            temp=heapArray.get((lastIndex-1)/2);
            if(temp<num){
                heapArray.set(lastIndex,temp);
                heapArray.set((lastIndex-1)/2,num);
            }
            else{
                bool=false;
            }
            lastIndex=(lastIndex-1)/2;
        }
    }
    public int deleteElement(){
        int temp;
        int deletedElement=-1;
        int size=heapArray.size();
        if(size==0){
            System.out.println("Heap is Empty deletion cannot be done");
        }
        else if(size==1){
            deletedElement=heapArray.get(0);
            heapArray.clear();
        }
        else{
            deletedElement=heapArray.get(0);
            temp=heapArray.get(size-1);
            heapArray.set(0,temp);
            heapArray.remove(size-1);
            if(heapArray.size()>1) 
                Heapify();
        }

        return deletedElement;
    }
    public void Heapify(){
        boolean bool=true;
        int parent=0;
        int parentElement,leftChild,rightChild;

        while(bool){ 
            if((parent*2)+2<=(heapArray.size()-2)/2){
                parentElement=heapArray.get(parent);
                leftChild=heapArray.get((parent*2)+1);
                rightChild=heapArray.get((parent*2)+2);
    
                if( leftChild >= rightChild ){
                    if(leftChild > parentElement){
                        heapArray.set(parent,leftChild);
                        heapArray.set((parent*2)+1,parentElement);
                        parent=parent*2+1;
                    }
                    else bool=false;
                }
                else{
                    if(rightChild > parentElement){
                        heapArray.set(parent,rightChild);
                        heapArray.set((parent*2)+2,parentElement);
                        parent = parent*2+2;
                    }
                    else bool=false;
                }
            }
            else {
                leftChild=heapArray.get((parent*2)+1);
                parentElement=heapArray.get(parent);
                if(leftChild > parentElement){
                    heapArray.set(parent,leftChild);
                    heapArray.set((parent*2)+1,parentElement);
                }
                bool=false;
            }
        }

    }
    public void display(){
        System.out.println(this.heapArray);
    }
    public static void main(String args[]){
        Heap maxHeap=new Heap();
        maxHeap.insertElement(10);
        maxHeap.insertElement(20);
        maxHeap.insertElement(30);
        maxHeap.insertElement(40);
        maxHeap.insertElement(50);
        maxHeap.insertElement(60);
        maxHeap.insertElement(70);
        maxHeap.display();
        System.out.println(maxHeap.deleteElement());
        maxHeap.display();
    }
}