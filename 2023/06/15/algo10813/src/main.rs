#![allow(unused)]
#![allow(non_snake_case)]
use std::{fs::File, io::{BufReader, Read, stdin}};

fn main() {
    let stdin = || {BufReader::new(File::open("./input.text").unwrap())};

    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let mut split = input.split_ascii_whitespace();
    let mut read = || split.next().unwrap().parse::<i32>().unwrap();
    let [Y,X] = [0;2].map(|_| read() as usize);
    let mut board = vec![0;Y];
    for i in 0..Y {
        board[i] = i + 1;
    }
    for j in 0..X {
        let [mut a, mut b] = [0;2].map(|_| read() as usize);
        a -= 1;
        b -= 1;
        let mut N = b - a + 1;
        let mut temp = vec![0;N];
        for i in 0..N {
            temp[i] = board[b - i];
        }
        for i in 0..N {
            board[a + i] = temp[i];
        }

    }
    for i in 0..Y {
        print!("{} ", board[i]);
    }
}
