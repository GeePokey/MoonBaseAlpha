printfn "Advent of Code 2020 Day 16"



// let filespec = "sample.day16.txt"
// let filespec = "sample2.day12.txt"
let filespec = "input.day16.txt"
let lines = System.IO.File.ReadAllLines(filespec) |> Array.toList
// let lines =  Array.map int lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )


// printfn "%A" lines

open System
open System.IO
open System.Text.RegularExpressions


let splitBy (c : string) f (str : string) = str.Split([| c |], StringSplitOptions.None) |> f
    

let (|Regex|_|) pattern input =
    let m = Regex.Match(input, pattern)
    if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
    else None

let validate_ticket (rules : (string*int*int*int*int) list) (fs:int []) =
    
     let sub  a (_, r1, r2, r3, r4) = (r1 <= a && a <= r2) || (r3 <= a && a <= r4) 
     let goodvalue q = rules |> List.exists (sub q)
     let badvalue q = not (goodvalue q)

     let z = fs |> Array.sumBy (fun a -> if badvalue a then a else 0 )
     printfn "%d <= %A   " z fs
     z

let dump_rules rules = for i in rules do
                         printfn "%A" i



open System.Collections.Generic


let mutable mymap = new Dictionary<int,  (string*int*int*int*int) >()

let update_mymap (newb:  seq< int * (string*int*int*int*int) list list > ) =
    let mutable updated = false    
    for i,f in newb do
        printfn "%d %A %A" i f (if f.Length = 1 then "Hit" else "-")
        for r in f do
            if r.Length = 1
            then
                mymap.[i] <- r.[0]
                updated <- true
    updated

let dump_map () =
    printfn "\nDump found"
    for i in mymap.Keys do
        printfn "%d %A" i mymap.[i]

let consolidate rules ( goodtickets : int [] list )=
    let pass  a (name, r1, r2, r3, r4) = (r1 <= a && a <= r2) || (r3 <= a && a <= r4)
    // seq of tickets list of fields list of rules that match
//    let byticket : seq< (string*int*int*int*int) list> = seq {

    printfn "\nGood Tickets found"
    // for i in goodtickets do
    //     printfn "%A" i

    let byticket : seq< (string*int*int*int*int) list list> = seq {
                           for ticket in goodtickets do
                              let passf = seq {
                                       for field in ticket do
                                       yield rules |> List.filter (pass field)
                                   }
                              yield (passf |> Seq.toList)
                       } 
    let byfield =
        seq {
            for i in 0..goodtickets.Head.Length-1 do
            yield Seq.toList ( seq { for t in byticket do yield t.[i]} )

            } |> Seq.indexed


(*
Dump ByField 
0 [[("row", 6, 11, 33, 44); ("class", 1, 3, 5, 7)];
 [("row", 6, 11, 33, 44); ("class", 1, 3, 5, 7)]] "-"
1 [[("class", 1, 3, 5, 7)]; [("class", 1, 3, 5, 7)]] "-"
2 [[("seat", 13, 40, 45, 50)]; [("seat", 13, 40, 45, 50)]] "-"
*)

    let filterbymap byfield =
        seq {
            for i, ff in byfield do
                yield i, Seq.toList (
                    seq {
                    for tt in ff do
                    yield List.filter (fun k -> not (mymap.ContainsValue k)) tt
                }
                    )
            }

    let mutable newb = filterbymap byfield
    while update_mymap newb do
        newb <- filterbymap newb

    dump_map ()


let rec handle_input codes rules ( accum : int [] list) : int [] list =
    match codes with
        | h::tail -> match h with
                       | Regex @"(.*): (\d+)-(\d+) or (\d+)-(\d+)" [name;a;b;c;d] -> handle_input tail ((name,int a, int b, int c, int d)::rules)  accum
                       | "" -> handle_input tail rules accum
                       | "your ticket:" -> handle_input tail rules accum
                       | "nearby tickets:" -> dump_rules rules
                                              handle_input tail rules accum
                       | Regex @"([0-9,]+)"  [str]         ->  let fields = (h.Split( [|","|], StringSplitOptions.None )) |> Array.map int
                                                               let subaccum = validate_ticket rules fields
                                                               if (subaccum > 0)
                                                               then handle_input tail rules accum
                                                               else handle_input tail rules (fields::accum)
                       | _ -> handle_input tail rules accum
                       
        | _ -> consolidate rules accum
               [ [| 0 |] ]


printfn "\n\npart2 handle_input \n%A" ( handle_input lines [] [] )

(*

part1 440; 788; 662; 555; 834; 527; 434;
  853; 854; 374; 555|]   
handle_input 22000 
        2.18 real         0.52 user         0.02 sys

Compilation finished at Tue Dec 15 22:27:09

*)

(*

for each ticket for each field - make a list of the rules it matches
for each field - if there is any list of length one - that must be the field rule.

 *)

 
