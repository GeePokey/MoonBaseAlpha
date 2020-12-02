printfn "Advent of Code Day 3"
// Day 3
let lines = System.IO.File.ReadAllLines("input.day2.txt") 
// printfn "%A" lines

type Rule = {rmin: int ; rmax : int; rletter: char ; rpassword: string }

let ra = seq { for i in lines do
                   let fields = i.Split(" ")
                   let rrange = fields.[0].Split("-")
                   yield { rmin = (System.Int32.Parse rrange.[0]) ;
                           rmax = (System.Int32.Parse rrange.[1]) ;
                           rletter = fields.[1].[0];
                           rpassword = fields.[2]  } }

let is_valid (case1: Rule) =
    let rcount = case1.rpassword |> Seq.filter (fun c -> c=case1.rletter) |> Seq.length
    (rcount >= case1.rmin ) && (rcount <= case1.rmax )

let is_valid2 (case1: Rule) =
    (if case1.rpassword.[case1.rmin - 1] = case1.rletter then not else id )
           (case1.rpassword.[case1.rmax - 1] = case1.rletter)

// for j in ra do printfn "%A %A" j (is_valid2 j)

printfn "Part1 %d " ( ra |> Seq.filter is_valid  |> Seq.length )
printfn "Part1 %d " ( ra |> Seq.filter is_valid2 |> Seq.length )
