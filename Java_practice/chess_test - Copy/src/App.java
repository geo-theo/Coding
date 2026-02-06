import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.util.Arrays;
import java.util.Scanner;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

public class App {


    static String[][] board =  {
                        { "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"},
                        { "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"},
                        { " ", " ", " ", " ", " ", " ", " ", " "},
                        { " ", " ", " ", " ", " ", " ", " ", " "},
                        { " ", " ", " ", " ", " ", " ", " ", " "},
                        { " ", " ", " ", " ", " ", " ", " ", " "},
                        { "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎", "♟︎"},
                        { "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"}
                    };
    
    static void printBoard(String[][] board){
        boolean flipper = true;
        System.out.println("   0  1  2  3  4  5  6  7  ");
        for(int i = 0; i < board.length; i++){
            System.out.print(i +" ");
            for(int j = 0; j < board[i].length; j++){
                flipper = !flipper; 
                if(board[i][j] != " "){
                    if(flipper){
                        System.out.print(" "+board[i][j]+" ");
                    }else{
                        System.out.print("█"+board[i][j]+"█");
                    }
                }else{
                    if(flipper){
                        System.out.print("   ");
                    }else{
                        System.out.print("███");
                    }
                }
            }
            flipper = !flipper;
            System.out.println();
        }
        
    }

    static void printHistory(String[][][] history){
        boolean flipper = true;

        for(int k = 0; k < history.length; k++){
            System.out.println("   0  1  2  3  4  5  6  7  ");
            for(int i = 0; i < history[k].length; i++){
                System.out.print(i +" ");
                for(int j = 0; j < history[k][i].length; j++){
                    flipper = !flipper; 
                    if(history[k][i][j] != " "){
                        if(flipper){
                            System.out.print(" "+history[k][i][j]+" ");
                        }else{
                            System.out.print("█"+history[k][i][j]+"█");
                        }
                    }else{
                        if(flipper){
                            System.out.print("   ");
                        }else{
                            System.out.print("███");
                        }
                    }
                }
                flipper = !flipper;
                System.out.println();
            }
        }
        
    }

    static void showUI(String[][] board){
        JFrame frame = new JFrame("Chess");

        frame.add(new JLabel("Chess w/o Rules", SwingConstants.CENTER), BorderLayout.NORTH);

        JPanel panel = new JPanel(new GridLayout(8,8));

        boolean flipper = true;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                JButton button = new JButton(String.valueOf(board[i][j]));
                panel.add(button);
            }
        }

        frame.add(panel, BorderLayout.CENTER);
        frame.setSize(500,500);
        frame.setVisible(true);

    }

    public static void main(String[] args) {
        String [][][] history = new String[3][8][8];


        Scanner scn = new Scanner(System.in);
        boolean playing = true;

        int current = 0;
        

        while(playing){
            printBoard(board);

            System.out.println("Please enter X coord:");
            int x = scn.nextInt();
            System.out.println("Please enter Y coord:");
            int y = scn.nextInt();

            if (x == -1 || y == -1 ){
                playing = false;
                break;
            }

            String temp = board[y][x];
            board[y][x] = " ";

            switch (temp) {
                case "♙":
                    //TODO
                    break;
                case "♟︎":
                    //TODO
                    break;
                case "♘": case "♞":
                    //TODO
                    break;
                case "♕": case "♛":
                    //TODO
                    break;
                case "♗": case "♝":
                    //TODO
                    break;
                case "♔": case "♚":
                    //TODO
                    break;
                case "♖": case "♜":
                    //TODO
                    break;
                default:
                    break;
            }
            
            System.out.println("Selected Piece: " + temp);
            System.out.println("Please enter X coord:");
            x = scn.nextInt();
            System.out.println("Please enter y coord:");
            y = scn.nextInt();

            board[y][x] = temp;

            history[current] = Arrays.copyOf(board, board.length);

            current++;
        }

        printHistory(history);

        scn.close();
    }
}