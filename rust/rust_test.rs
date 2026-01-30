fn main() {
  fn double(num: u128) -> u128 {
    num * 2
  }

  let int: i32 = 32;
  let big_int = 10;
  let float = 1.2;

  let outcome = double(big_int);
  let doubled_outcome = outcome;

  println!("doubled_outcome");
  
}
