printfn "Advent of Code 2020 Day 4"
// Day 4
// let lines = System.IO.File.ReadAllLines("input.day4.txt") 
let lines = System.IO.File.ReadAllLines("input.txt") 
// printfn "%A" lines

let len = lines |> Seq.length
let width = lines.[0] |> Seq.length
let x = 0
let y = 0

    

// let slope = seq {
//     for y in [1..len-1] do
//         let x = y * 3
//         if lines.[y].[y*3 % width] = '#' then yield 1 else yield 0
//     }
    
// printfn "Number of trees Part 1 %d " (slope |> Seq.sum )

                  

// Right 1, down 1.
// Right 3, down 1. (This is the slope you already checked.)
// Right 5, down 1.
// Right 7, down 1.
// Right 1, down 2.

let slope xm ym = seq {
    printfn "%A %A" xm ym
    for i in [1..(len-1)/ym] do
        let y = i * ym
        let x = i * xm  % width
        if lines.[y].[x] = '#' then yield 1 else yield 0
    }
    

printfn "Number of trees Part 1 %d (237) 9:10 PM " (slope 3 1 |> Seq.sum )

let r1d1 = slope 1 1 |> Seq.sum
let r3d1 = slope 3 1 |> Seq.sum
let r5d1 = slope 5 1 |> Seq.sum
let r7d1 = slope 7 1 |> Seq.sum
let r1d2 = slope 1 2 |> Seq.sum
let allm = r1d1 * r3d1 * r5d1 * r7d1 * r1d2

printfn "Number of trees all slopes Part 2 (2106818610) %d  9:18 PM!!  " allm
