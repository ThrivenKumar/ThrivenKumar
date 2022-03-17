class binarySearch{

    public static void main(String args[]){

        int numbers[]=new int[]{1,2,3,4,5,6,7,8,9,10,11,12};
        int key=-1;
        int left=0;
        int right=numbers.length-1;
        int mid=right/2;
        while (left<=right){
            if (numbers[mid]==key){
                System.out.println("Found at Index: "+ mid);
                return;
            }
            else if(numbers[mid]>key){
                right=mid-1;
                mid=(left+right)/2;
            }
            else{
                left=mid+1;
                mid=(left+right)/2;
            }
        }
        System.out.println("Element Not found");
    }
}