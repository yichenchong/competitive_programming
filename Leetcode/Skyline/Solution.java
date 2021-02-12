import java.awt.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
import java.io.*;
/**
 * Write a description of class Solution here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Solution
{
    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static int[][] skylineProblem(int[][] buildings)
    {
        int[] buildingEdges=new int[buildings.length*2];
        for(int i=0;i<buildings.length;i++) {
            buildingEdges[i*2]=buildings[i][0];
            buildingEdges[i*2+1]=buildings[i][1];
        }
        Arrays.sort(buildingEdges);
        HashMap<Integer,Integer> edgeMap=new HashMap<Integer,Integer>();
        for(int i=0;i<buildingEdges.length;i++) {
            int edge=buildingEdges[i];
            ArrayList buildingsHeight=new ArrayList<String>();
            for(int j=0;j<buildings.length;j++) {
                int[] building=buildings[j];
                if(buildingAt(building,edge)) buildingsHeight.add(building[2]);
            }
            int maxHeight=maxHeight(buildingsHeight);
            edgeMap.put(edge,maxHeight);
        }
        ArrayList<int[]> coords=new ArrayList<int[]>();
        int prevHeight=0;
        for(int i=0;i<buildingEdges.length;i++) {
            int curEdge=buildingEdges[i];
            if(edgeMap.get(curEdge)!=prevHeight) {
                int[] coord=new int[] {curEdge,edgeMap.get(curEdge)};
                coords.add(coord);
                prevHeight=edgeMap.get(curEdge);
            }
        }
        int[][] coordsArray=listToArray(coords);
        return coordsArray;
    }
    public static boolean buildingAt(int[] building,int value) {
        if(building.length!=3) throw new RuntimeException();
        int buildingStart=building[0];
        int buildingEnd=building[1];
        return value>=buildingStart&&value<buildingEnd;
    }
    public static int maxHeight(ArrayList<Integer> heights) {
        int max=0;
        for(int i=0;i<heights.size();i++) if(heights.get(i)>max) max=heights.get(i);
        return max;
    }
    public static int[][] listToArray(ArrayList<int[]> coords) {
        int[][] array=new int[coords.size()][];
        for(int i=0;i<coords.size();i++) {
            array[i]=coords.get(i);
        }
        return array;
    }
}
