printfn "Advent of Code Day 3"
// Day 3
let lines = System.IO.File.ReadAllLines("input.day2.txt") 
// printfn "%A" lines

type Rule = {rmin: int ; rmax : int; rletter: char ; rpassword: string }

let ra = seq { for i in lines do
                   let fields = i.Split(" ")
                   let rrange = fields.[0].Split("-")
                   yield { rmin = (System.Int32.Parse rrange.[0]) ;
                           rmax = (System.Int32.Parse rrange.[1] );
                           rletter = fields.[1].[0];
                           rpassword = fields.[2]  }
               }
//     printfn "%A %A %A" (fields.[0].Split("-")) fields.[1] fields.[2]

let is_valid (case1: Rule) =
    let rcount = case1.rpassword |> Seq.filter (fun c -> c=case1.rletter) |> Seq.length
    (rcount >= case1.rmin ) && (rcount <= case1.rmax )

let xis_valid2 (case1: Rule) =
    let x = (case1.rmin - 1)
    let y = (case1.rmax - 1)
    let len = (String.length case1.rpassword)
    if len < x
    then false
    else if case1.rpassword.[x] = case1.rletter
         then if len < y || not (case1.rpassword.[y] = case1.rletter)
              then true
              else not (case1.rpassword.[y] = case1.rletter)
         else if len < y || (case1.rpassword.[y] = case1.rletter)
              then false
              else true

let is_valid2 (case1: Rule) =
    let x = (case1.rmin - 1)
    let y = (case1.rmax - 1)
    let len = (String.length case1.rpassword)
    if len < x
    then false
    else if case1.rpassword.[x] = case1.rletter
         then not (case1.rpassword.[y] = case1.rletter)
         else (case1.rpassword.[y] = case1.rletter)


for j in ra do printfn "%A %A" j (is_valid2 j)

printfn "Part1 %d " ( ra |> Seq.filter is_valid |> Seq.length )
printfn "Part1 %d " ( ra |> Seq.filter is_valid2 |> Seq.length )
