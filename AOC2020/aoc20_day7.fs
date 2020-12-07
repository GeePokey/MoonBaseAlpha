printfn "Advent of Code 2020 Day 7"
// Day 7
let lines = System.IO.File.ReadAllLines("input.day7.txt") 
// let lines = System.IO.File.ReadAllLines("D4_kinput.txt") 
// let lines = System.IO.File.ReadAllLines("input.txt")
// let lines = System.IO.File.ReadAllLines("sample.day7.txt") 
// printfn "%A" lines


(*
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
*)

type Bag = string
type count_bag  = {  count:int; btype:Bag }
type rule = { bagcolor:Bag; count_bag: count_bag list }
type containedby = { bagcolor:Bag; bigbags: Bag list }





open System.Text.RegularExpressions
let input2 = "dotted black bags contain no other bags."

let nob = "(\w+\s\w+)\sbags contain no other bags."

let m2 = Regex.Match(input2, nob)
printfn "%A" (if m2.Success then Some(List.tail [ for g in m2.Groups -> g.Value ])
                            else None)


// let input = "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags."
// let   pattern = "(\w+\s\w+)\sbags contain (([\d]+)\s(\w+\s\w+)(\sbags,\s([\d]+)\s(\w+\s\w+))*\sbags.)"
// let input = "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags, 1 qq ww bag."
// let pattern = "(\w+\s\w+)\sbags contain (([\d]+)\s(\w+\s\w+)(\sbags?,\s([\d]+)\s(\w+\s\w+))*\sbags?.)"

let sinput = "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags, 1 qq ww bag, 3 zz ww bags."
let ssinput = "vibrant plum bags contain 5 faded blue bag, 6 dotted black bag, 1 qq ww bag, 3 zz ww bag."
let input = "vibrant plum bags contain 5 faded blue bags."
let pattern = "(\w+\s\w+)\sbags contain ([\d]+)\s(\w+\s\w+)(?:\sbags?,\s([\d]+)\s(\w+\s\w+))?(?:\sbags?,\s([\d]+)\s(\w+\s\w+))?(?:\sbags?,\s([\d]+)\s(\w+\s\w+))?(?:\sbags?,\s([\d]+)\s(\w+\s\w+))?\sbags?."



let m = Regex.Match(input, pattern)
printfn "%A" (if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
                           else None)


(*
Some ["vibrant plum"; "5"; "faded blue"; "6"; "dotted black"; "1"; "qq ww"; "3";   "zz ww"; ""; ""]
     ["vibrant plum"; "5"; "faded blue"; "6"; "dotted black"; "1"; "qq ww"; "3";   "zz ww"; ""; ""]
Some ["vibrant plum"; "5"; "faded blue"; ""; ""; ""; ""; ""; ""; ""; ""]
*)

let mutable containers = Map.empty<Bag,Bag list>

for r in lines do
    printfn "line %A " r
//    let nob = Regex.Match(input, nobagpattern)
    let m = Regex.Match(r, pattern )
    if m.Success
    then
        let skip::container::tail =  [ for g in m.Groups -> g.Value ]
        for g in tail do
            // printfn "g is %A -> %A" g container
            if containers.ContainsKey(g)
            then containers <- containers.Add( g, container :: containers.[g] )
            else containers <- containers.Add( g, [container] )
            
printfn "%A" containers

let mutable answer = Set.empty

let rec find_all_nest_containers containerlist =
    printfn "CL %A" containerlist
    match containerlist with
        | h::tail -> answer <- answer.Add( h )
                     if  (containers.ContainsKey h)
                     then
                         find_all_nest_containers containers.[h]
                     find_all_nest_containers tail

        | [] -> ()

find_all_nest_containers  containers.["shiny gold"]
printfn "containing folders %A" (answer |> Seq.length )


(*

                          
CL []
CL []
containing folders 131  Correct!!
        4.20 real         0.41 user         0.02 sys

Compilation finished at Sun Dec  6 23:15:40

*)
