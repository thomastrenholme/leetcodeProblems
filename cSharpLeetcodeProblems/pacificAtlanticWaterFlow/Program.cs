using System;
using System.Collections.Generic;
public class Solution {

    public static void Main(string[] args){

    }
    public IList<IList<int>> PacificAtlantic(int[][] heights) {
        
        int nRows = heights.Length;
        int nCols = heights[0].Length;


        HashSet<Tuple<int, int>> pacificSet = new HashSet<Tuple<int, int>>();
        HashSet<Tuple<int, int>> atlanticSet = new HashSet<Tuple<int, int>>();


        void dfs(int i, int j, HashSet<Tuple<int, int>> visited, int prevHeight){

            if(i < 0 || i==nRows || j < 0 || j==nCols || visited.Contains((i, j).ToTuple()) ||
            prevHeight < heights[i][j]){
                return; //exit dfs
            }

            //add to pacific or atlantic set
            //dfs east, west, north, south to all neighboring islands
            visited.Add((i, j).ToTuple());
            dfs(i +1, j, visited, heights[i][j]);
            dfs(i -1, j, visited, heights[i][j]);
            dfs(i, j+1, visited, heights[i][j]);
            dfs(i, j-1, visited, heights[i][j]);
        }


        for(int x = 0; x < nRows; x++){

            //pacific dfs
            dfs(x, 0, pacificSet, heights[x][0]);
            //atlantic dfs
            dfs(x, nCols-1, atlanticSet, heights[x][nCols-1]);
        }
        for(int y = 0; y < nCols; y++){

            //pacific dfs
            dfs(0, y, pacificSet, heights[0][y]);

            //atlantic dfs
            dfs(nRows-1, y, atlanticSet, heights[nRows-1][y]);
        }
        foreach(Tuple<int, int> t in pacificSet){
            Console.Write(t);
        }
        foreach(Tuple<int, int> t in atlanticSet){
            Console.WriteLine(t);
        }
        IEnumerable<Tuple<int, int>> retSet = new List<Tuple<int, int>>();
        foreach(Tuple<int, int> t in pacificSet){
            if(atlanticSet.Contains(t)){
                retSet.Add(t);
            }
        }
        List<int[]> retArr = new List<int[]>();
        foreach(Tuple<int, int> t in retSet){
            retArr.Add(new int[]{t.Item1, t.Item2});
        }
        return retArr.Cast<IList<int>>().ToList();
    }
}