public class Solution {
    public int racecar(int target) {
        return stepsOptimized(target);
    }
    public static int min(int a,int b) {
        if(a<b) return a;
        else return b;
    }
    public static int min(int a,int b,int c) {
        return min(min(a,b),c);
    }
    public static int min(int a,int b,int c,int d) {
        return min(min(a,b,c),d);
    }
    public static int min(int a,int b,int c,int d,int e) {
        return min(min(a,b,c,d),e);
    }
    public static int min(int a,int b,int c,int d,int e,int f) {
        return min(min(a,b,c,d,e),f);
    }
    
    public static int stepsOptimized(int distanceToTarget) {
        int newNum=0,prevNum=0,count=0,target=distanceToTarget,i;
        for(i=0;i<1000;i++) {
            newNum=(int)Math.pow(2,i)+prevNum;
            prevNum=newNum;
            count++;
            if(newNum*2+1>target) break;
        }
        int nextNumOverShoot = (int)Math.pow(2,++i)+prevNum;
        if(newNum==distanceToTarget) return count;
        else if(target-newNum>15) return min(2+count+stepsOptimized(target-newNum),2+count+stepsOptimized(nextNumOverShoot-target),3+count+stepsOptimized(target-newNum+1),4+count+stepsOptimized(target-newNum+3),5+count+stepsOptimized(target-newNum+7),6+count+stepsOptimized(target-newNum+15));
        else if(target-newNum>3) return min(2+count+stepsOptimized(target-newNum),2+count+stepsOptimized(nextNumOverShoot-target),3+count+stepsOptimized(target-newNum+1),4+count+stepsOptimized(target-newNum+3));
        else if(target-newNum!=1) return min(2+count+stepsOptimized(target-newNum),2+count+stepsOptimized(nextNumOverShoot-target),3+count+stepsOptimized(target-newNum+1));
        else {
            return min(2+count+stepsOptimized(target-newNum),2+count+stepsOptimized(nextNumOverShoot-target));
        }
    }
}