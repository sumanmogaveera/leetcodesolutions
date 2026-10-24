class Solution {
    public int findNumbers(int[] nums) {
       int count=0;
       for(int num:nums){
        String digit=Integer.toString(num);
        if(digit.length()%2==0){
            count++;
        }
       }
       return count;
    }
}