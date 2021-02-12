import java.awt.List;

/**
 * Write a description of class Skyline here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Skyline
{
    public static void main(String[] args)
    {
        int[] building1=new int[]{2,9,10},building2=new int[]{3,7,15},building3=new int[]{5,12,12},building4=new int[]{15,20,10},building5=new int[]{19,24,8};
        int[][] buildingsArray1=new int[][]{building1,building2,building3,building4,building5};
        int[][] solution=Solution.skylineProblem(buildingsArray1);
        printArray(solution);
    }
    public static String printArray(int[] array) {
        String outputString="[";
        for(int i=0;i<array.length;i++) {
            outputString+=array[i]+",";
        }
        outputString=outputString.substring(0,outputString.length()-1);
        outputString+="]";
        return outputString;
    }
    public static void printArray(int[][] array) {
        String outputString="[";
        for(int i=0;i<array.length;i++) {
            outputString+=printArray(array[i])+",";
        }
        outputString=outputString.substring(0,outputString.length()-1);
        outputString+="]";
        System.out.println(outputString);
    }
}
