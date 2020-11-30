printfn "day 16"

// let input = [| 5;9;7;7;7;3;7;3;0;2;1;2;2;2;6;6;8;7;9;8;5;6;7;8;0;2;1;3;3;4;1;3;7;8;2;8;9;0;2;7;4;1;2;7;4;0;8;9;5;1;0;0;8;3;3;1;6;8;3;3;4;5;3;3;9;7;2;0;1;2;2;0;1;3;1;6;3;8;7;9;4;8;1;7;8;1;8;5;2;6;7;4;5;9;3;8;4;8;2;8;6;0;2;8;4;3;3;1;3;7;5;8;1;1;0;6;0;4;0;0;7;0;1;8;0;5;1;1;3;3;6;0;2;5;3;1;5;3;1;5;3;6;9;5;4;7;1;3;1;5;8;0;0;3;8;5;2;6;1;9;4;1;5;0;2;1;8;8;3;1;1;2;7;2;6;3;6;4;4;3;8;6;3;6;3;6;2;8;6;2;2;1;9;9;1;8;5;8;4;1;1;0;4;2;4;7;6;2;3;1;4;5;8;8;7;8;2;0;1;4;3;7;0;1;0;7;1;8;7;3;1;5;3;0;1;1;0;6;5;9;7;2;4;4;2;4;5;2;0;2;5;4;6;7;9;7;3;4;4;7;9;7;8;6;2;44;4;4;9;8;6;3;6;7;3;6;9;0;8;5;7;6;8;0;1;8;7;8;7;9;8;0;6;2;6;7;5;0;9;3;4;5;0;4;1;0;1;4;8;2;5;4;7;0;5;6;9;1;9;5;7;0;6;8;4;8;4;2;7;2;9;7;8;7;2;8;9;2;4;2;5;2;5;0;0;6;4;0;0;0;6;0;6;7;4;6;5;1;9;4;0;0;4;2;4;3;4;0;9;8;8;4;6;6;1;0;2;8;2;4;6;7;5;2;9;1;4;5;5;4;1;0;9;9;8;8;7;4;8;3;2;1;2;9;8;0;7;8;0;4;8;7;2;9;1;5;2;9;2;8;9;2;7;2;5;5;3;9;5;9;0;8;8;3;7;6;6;0;1;2;3;4;5;9;5;0;0;2;7;8;5;1;5;6;4;9;0;4;8;6;9;8;9;0;0;1;9;4;9;0;7;9;4;7;6;6;2;4;7;9;5;2;5;3;0;7;5;3;1;5;1;3;7;3;1;8;4;8;2;0;5;0;3;7;6;6;8;0;8;6;4;5;2;8;8;6;4;8;2;5;1;0;0;5;5;3;1;4;0;5;4;1;1;5;9;6;8;4;9;2;2;9;0;3;4;0;1;8;5;2;1;0;1;1;8;6;0;2;8;0;7;6;4;4;8;6;6;1;6;9;5;0;0;3;3;9;4;4;9;1;6;9;2;4;1;9;9;6;4;3;6;6;8;6;0;5;6;5;6;3;9;6;0;0;4;3;0;4;4;0;5;8;1;1;4;7;0;8;5;6;3;4;5;0;7;4;1;7;6;2;1;9;8;6;6;6;8;5;4;9;2;3;3;7;9;7;8;4;8 |]


// let input = [| 5;9;7;7;7;3;7;3;0;2;1;2;2;2;6;6;8;7;9;8;5;6;7;8;0;2;1;3;3;4;1;3;7;8;2;8;9;0;2;7;4;1;2;7;4;0;8;9;5;1;0;0;8;3;3;1;6;8;3;3;4;5;3;3;9;7;2;0;1;2;2;0;1;3;1;6;3;8;7;9;4;8;1;7;8;1;8;5;2;6;7;4;5;9;3;8;4;8;2;8;6;0;2;8;4;3;3;1;3;7;5;8;1;1;0;6;0;4;0;0;7;0;1;8;0;5;1;1;3;3;6;0;2;5;3;1;5;3;1;5;3;6;9;5;4;7;1;3;1;5;8;0;0;3;8;5;2;6;1;9;4;1;5;0;2;1;8;8;3;1;1;2;7;2;6;3;6;4;4;3;8;6;3;6;3;6;2;8;6;2;2;1;9;9;1;8;5;8;4;1;1;0;4;2;4;7;6;2;3;1;4;5;8;8;7;8;2;0;1;4;3;7;0;1;0;7;1;8;7;3;1;5;3;0;1;1;0;6;5;9;7;2;4;4;2;4;5;2;0;2;5;4;6;7;9;7;3;4;4;7;9;7;8;6;2;4;4;4;4;9;8;6;3;6;7;3;6;9;0;8;5;7;6;8;0;1;8;7;8;7;9;8;0;6;2;6;7;5;0;9;3;4;5;0;4;1;0;1;4;8;2;5;4;7;0;5;6;9;1;9;5;7;0;6;8;4;8;4;2;7;2;9;7;8;7;2;8;9;2;4;2;5;2;5;0;0;6;4;0;0;0;6;0;6;7;4;6;5;1;9;4;0;0;4;2;4;3;4;0;9;8;8;4;6;6;1;0;2;8;2;4;6;7;5;2;9;1;4;5;5;4;1;0;9;9;8;8;7;4;8;3;2;1;2;9;8;0;7;8;0;4;8;7;2;9;1;5;2;9;2;8;9;2;7;2;5;5;3;9;5;9;0;8;8;3;7;6;6;0;1;2;3;4;5;9;5;0;0;2;7;8;5;1;5;6;4;9;0;4;8;6;9;8;9;0;0;1;9;4;9;0;7;9;4;7;6;6;2;4;7;9;5;2;5;3;0;7;5;3;1;5;1;3;7;3;1;8;4;8;2;0;5;0;3;7;6;6;8;0;8;6;4;5;2;8;8;6;4;8;2;5;1;0;0;5;5;3;1;4;0;5;4;1;1;5;9;6;8;4;9;2;2;9;0;3;4;0;1;8;5;2;1;0;1;1;8;6;0;2;8;0;7;6;4;4;8;6;6;1;6;9;5;0;0;3;3;9;4;4;9;1;6;9;2;4;1;9;9;6;4;3;6;6;8;6;0;5;6;5;6;3;9;6;0;0;4;3;0;4;4;0;5;8;1;1;4;7;0;8;5;6;3;4;5;0;7;4;1;7;6;2;1;9;8;6;6;6;8;5;4;9;2;3;3;7;9;7;8;4;8 |]

// let offset = 0

// let inputx1 = [|1;2;3;4;5;6;7;8|]
// let inputx1 = [|8;0;8;7;1;2;2;4;5;8;5;9;1;4;5;4;6;6;1;9;0;8;3;2;1;8;6;4;5;5;9;5|]

// let input = [| 1;9;6;1;7;8;0;4;2;0;7;2;0;2;2;0;9;1;4;4;9;1;6;0;4;4;1;8;9;9;1;7 |]

// let input = [|6;9;3;1;7;1;6;3;4;9;2;9;4;8;6;0;6;3;3;5;9;9;5;9;2;4;3;1;9;8;7;3 |]


// part 2
let inputx1 = [|0;3;0;3;6;7;3;2;5;7;7;2;1;2;9;4;4;0;6;3;4;9;1;5;6;5;4;7;4;6;6;4|]
let offset = 303673

let input = seq {for _ in 1..10000 do yield! inputx1 } |> Seq.toArray
// let input = seq {for _ in 1..1000 do yield! inputx1 } |> Seq.toArray
// let input = seq {for _ in 1..1 do yield! inputx1 } |> Seq.toArray

let ll = Array.length input

printfn "part2 %d %A" ll input

let pat = [|0;1;0;-1|]

let patgen i = seq { for p in pat do
                        for _ in 0..i do
                            yield p } |> Seq.toArray


    
// the pattern is 4 * k  long
// the offset is (i + 1) % (4 * k)
// the value is pat.[offset / k]

let coef k i = pat.[ ((i + 1) % (4*(k+1))) /(k+1)]

// for j in 0..20 do
//      printfn "%5d %5d %5d" j (coef 0 j) (coef 3 j)
    
printfn "%A" ( patgen 0)
// printfn "%A" ( patgen 1)
// printfn "%A" ( patgen 2)
// printfn "%A" ( patgen 3)
// printfn "%d" (abs (-17 % 10))



let mydot2 k  (data:int array) =
    abs([|0..(ll-1)|] |> Array.sumBy (fun i -> data.[i] * (coef k i ) )) % 10




// let mutable minput = Array.copy input
// let thenumbers = [|0..(ll-1)|]

printfn "Start the loop"

// for g in 1..100 do
//     minput <- (thenumbers |> Array.map (fun i ->
//                                            abs( thenumbers |> Array.sumBy (fun w -> minput.[w] * (coef i w ) )) % 10 ))
    
// //    printf  "%d %A  Answer: " g minput.[offset..offset+7]
//     printf  "%d %A  Answer: " g minput.[..7]
//     for dig in  minput.[0..7] do
//           printf "%d" dig
//     printfn ""

// before inlining
// for g in 1..100 do
//     minput <- ([|0..(ll-1)|] |> Array.map (fun i -> mydot2  i minput ))
    
//     printf  "%d %A  Answer: " g minput.[offset..offset+7]
//     for dig in  minput.[offset..offset+7] do
//           printf "%d" dig
//     printfn ""
let mydot (pat: int array) (data:int array) =
     let pp = Array.length pat
     // printfn "%A" ([|0..(ll-1)|] |> Array.map (fun i -> data.[i] * pat.[i%pp]) ) 
     abs([|0..(ll-1)|] |> Array.sumBy (fun i -> data.[i] * pat.[(i+1)%pp]) ) % 10

                         
// printfn "%d" (mydot (patgen 0) input)

let mydot3 kk (data:int array) =
    // just sum segments of data
    // let k = position
    let k = kk + 1
    let minuses = k * 2  // offset from 1' to -1's
    let plus_ones = k - 1
    let plus_minuses = minuses + plus_ones
    let start = k - 1
    let datalen = Array.length data
    let result = Seq.sum (seq { for ones in start .. k * 4 .. datalen-1 do
                                    let one_end   = min (datalen-1) (ones + plus_ones)
                                    let minus_end = min (datalen-1) (ones + plus_minuses)
                                    // printfn "  1: %A %d %d" ( data.[ ones .. one_end ]) ones one_end
                                    // printfn "  2:    %d %d" (ones + minuses )  minus_end 
                                
                                    if (ones + minuses) < datalen
                                    then
                                       // printfn "  2: %A %d %d" ( data.[ (ones + minuses) .. (minus_end) ]) (ones + minuses ) ( minus_end)
                                       yield (Array.sum data.[ ones .. one_end ]) - (Array.sum data.[ (ones + minuses) .. minus_end ])
                                    else
                                       yield (Array.sum data.[ ones .. one_end ])
                                })
    

    (abs result) % 10


let result = ([|0..(ll-1)|] |> Array.map (fun i -> mydot (patgen i) input ))
let result3 = ([|0..(ll-1)|] |> Array.map (fun i -> mydot3  i input ))



printfn "result   %A"  (result)
printfn "result3  %A"  (result3)



let mutable minput = Array.copy input

// for g in 1..100 do
//     minput <- ([|0..(ll-1)|] |> Array.map (fun i -> mydot2  i minput ))
    

// printf  "100 %A  Answer: "  minput.[offset..offset+7]
// for dig in  minput.[offset..offset+7] do
//     printf "%d" dig
// printfn ""

// minput <- Array.copy input

for g in 1..100 do
    minput <- ([|0..(ll-1)|] |> Array.map (fun i -> mydot3  i minput ))
    printfn "%d" g
    

printf  "100 %A  Answer: "  minput.[offset..offset+7]
for dig in  minput.[offset..offset+7] do
    printf "%d" dig
printfn ""


(*
   100 [|9; 0; 3; 4; 6; 9; 5; 3; 6; 7; 3; 3; 2; 4; 1; 6; 1; 4; 3; 2; 1; 7; 6; 8; 4; 3;
  7; 2; 7; 5; 0; 2; 5; 5; 8; 0; 4; 1; 8; 9; 1; 4; 3; 6; 7; 2; 6; 9; 1; 0; 7; 5;
  9; 3; 3; 2; 6; 9; 0; 6; 1; 5; 1; 2; 1; 8; 2; 6; 7; 5; 0; 5; 6; 9; 0; 5; 6; 9;
  9; 4; 6; 1; 1; 4; 4; 3; 1; 4; 9; 7; 7; 0; 5; 1; 1; 5; 6; 1; 9; 6; ...|]
        3.90 real         3.54 user         0.35 sys

Compilation finished at Sun Dec 15 21:42:31


90346953

That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 90346953.) [Return to Da



 100 [|5; 3; 2; 9; 6; 0; 8; 2|]
        3.42 real         3.06 user         0.35 sys

Compilation finished at Sun Dec 15 21:53:25

53296082  correct
        3.42 real         3.06 user         0.35 sys

Compilation finished at Sun Dec 15 21:53:25



part 2
03036732577212944063491565474664


2 * 650 = 1300 = /4 = 13*25

find lcm between pattern len and 650 - then multiple it out?

*)




break
