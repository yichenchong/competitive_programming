
/**
 * Write a description of class Insomnia here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Insomnia
{
    // instance variables - replace the example below with your own

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static void main(String[] args)
    {
        // put your code here
        System.out.println(test(89));
        System.out.println(test(45));
        System.out.println(test(123));
        System.out.println(test(99));
        System.out.println(test(79));
        System.out.println(test(0));
    }
    public static String test(int num) {
        boolean[] numsCovered=new boolean[10];
        for(int i=0;i<numsCovered.length;i++) numsCovered[i]=false;
        int multiplier=1;
        while(!allTrue(numsCovered)&&multiplier<=200*num) {
            int newNum=num*multiplier;
            while(newNum>0) {
                int curDig=newNum%10;
                if(!numsCovered[curDig]) numsCovered[curDig]=true;
                newNum/=10;
            }
            int oldNum=num*multiplier;
            if(allTrue(numsCovered)) return ""+oldNum;
            multiplier++;
        }
        return "INSOMNIA";
    }
    public static boolean allTrue(boolean[] arr) {
        for(int i=0;i<arr.length;i++) if(!arr[i]) return false;
        return true;
    }
}
