use std::time::SystemTime;

fn linreg(x:Vec<f32>, y:Vec<f32>, z:f32) -> f32 {
    x.iter().zip(y.iter()).fold(0.0, |acc, z| acc + z.0 * z.1) + z
    
    
}

fn main(){
    let start = SystemTime::now();
    for _i in 0..1000000{
        linreg(vec![2.4,6.9], vec![2.9, 4.4], 2f32);
    }
    println!("Miliseconds: {:?}", start.elapsed().unwrap().as_millis());
}
