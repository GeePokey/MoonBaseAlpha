printfn "Advent of Code 2020 Day 14"



// let filespec = "sample.day14.txt"
// let filespec = "sample2.day14.txt"
let filespec = "input.day14.txt"
let lines = System.IO.File.ReadAllLines(filespec) |> Array.toList
// let lines =  Array.map int lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )


// printfn "%A" lines
(*
                  
For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
This program starts by specifying a bitmask (mask = ....). The mask it specifies will overwrite two bits in every written value: the 2s bit is overwritten with 0, and the 64s bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)
So, because of the mask, the value 73 is written to memory address 8 instead. Then, the program tries to write 101 to address 7:

value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)
This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. Finally, the program tries to write 0 to address 8:

value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)
64 is written to address 8 instead, overwriting the value that was there previously.

To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. (The entire 36-bit address space begins initialized to the value 0 at every address.) In the above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a sum of 165.


                  *)



(* sample works
t Sun Dec 13 22:17:03

make -k 14.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc 14.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono 14.exe
Advent of Code 2020 Day 14
"mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
New emask 000000000000000000000000000000000010 = 0b000000000000000000
New emask 000000000000000000000000000000000010 = 000000000002 = 000000 000002
New emask 000000000000000000000000000001000000 = 0b000000000000000000
New emask 000000000000000000000000000001000000 = 000000000040 = 000000 000040
"mem[8] = 11"
"mem[7] = 101"
"mem[8] = 0"
part1 sample.day14.txt 165L
seq [[8, 64]; [7, 101]]
        0.19 real         0.16 user         0.01 sys

Compilation finished at Sun Dec 13 22:17:07


"mask = 110X0010110X1X100010101X00100X001010"
New emask 001011010010000111010100110110110101 = 0b001011010010000111
New emask 001011010010000111010100110110110101 = 0002D21D4DB5 = 00B487 014DB5
New emask 110000101100101000101010001000001010 = 0b110000101100101000
New emask 110000101100101000101010001000001010 = 000C2CA2A20A = 030B28 02A20A
"mem[30968] = 2095418"
"mem[3121] = 139148"
"mem[53666] = 26824"
part1_input.day14.txt: 16003257187056L
seq
  [[40278, 47784937127]; [51306, 38797334875]; [31036, 47782840231];
   [8433, 36719102986]; ...]
        1.98 real         0.23 user         0.02 sys

Compilation finished at Sun Dec 13 22:18:08

*)

open System.Text.RegularExpressions

let (|Regex|_|) pattern input =
    let m = Regex.Match(input, pattern)
    if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
    else None

open System.Collections.Generic
let mutable vmem = new Dictionary<int64,int64>()

let bin2int64 (ss:string) key =
    let s = ss.Replace(key,"+").Replace("X","0").Replace("0","0").Replace("1","0").Replace("+","1")
    //    printfn "New emask %s = %s" s  ("0b" + s.[..17])
    let upperbits = int64 (int ("0b" + s.[..17]))
    let lowerbits = int64 (int ("0b" + s.[18..]))
    let result = (upperbits <<< 18) + lowerbits
    //    printfn "New emask %s = %012X = %06X %06X" s result upperbits lowerbits
    result


let duplexmask (ss:string) =
    let zeromask = bin2int64 ss "0"
    let inverted = ~~~ zeromask
    let onesmask = bin2int64 ss "1"
    inverted, onesmask


let rec travel code (mask:int64 * int64) =
      match code with
        | h::tail -> // printfn "%A" h
                     match h with
                       | Regex @"mask\s*=\s*([X01]+)" [maskv] -> travel tail (duplexmask maskv)
                       | Regex @"mem\s*\[([\d]+)\]\s*=\s*([0-9]+)" [addr;sval] -> vmem.[int64 addr] <- (int64 sval) &&& (fst mask) ||| (snd mask)
                                                                                  travel tail mask
                       | _ -> printfn "ERROR: non code %s" h
        | _  -> printfn "part1_%s: %A (16003257187056)" filespec (vmem.Values |> Seq.sum)


travel lines (0L,0L) // Part 1








// Constants
let Zero64 = int64 0
let One64 = int64 1

vmem <- new Dictionary<int64,int64>()  // Reset the memory array.


let nth_bit_of n (addr:int64) =
    ( addr >>> n ) &&& (int64 1)
    
let rec vmem_mask_write addr value (maskstr: char list)  addrmaskval =
    // printfn "   vmem_mask_write %X %d %X %A len %d bit %d" addr value addrmaskval ( if maskstr.IsEmpty then '_' else maskstr.Head) maskstr.Length (nth_bit_of (-1 + Seq.length maskstr) addr)

    // Take one character from front of maskstr, and append one bit to addrmaskval for each recursion.
    // When maskstr is empty, write the value to the calculated addrmaskval.
    
    match maskstr with
        | h::tail  ->  let addrmaskval = (addrmaskval <<< 1) + (match h with
                                                                | '1' -> One64
                                                                | '0' -> nth_bit_of (-1 + Seq.length maskstr) addr
                                                                | 'X' -> Zero64
                                                                | _ -> printfn "ERROR: bad mask maskstr %A" maskstr
                                                                       Zero64
                                                               )

                       // Recurse with both '0' and '1' variations if the current mask is X
                       vmem_mask_write addr value tail addrmaskval
                       if h = 'X' then vmem_mask_write  addr value tail (addrmaskval ||| One64)
                       
        | _        ->  vmem.[addrmaskval] <- value
                       // printfn "vmem_mask_write %X %d ACTUAL\n" addrmaskval value
            

let rec travel2 code (mask:string) =
      match code with
        | h::tail -> // printfn "%A" h
                     match h with
                       | Regex @"mask\s*=\s*([X01]+)" [maskv] -> travel2 tail maskv
                       | Regex @"mem\s*\[([\d]+)\]\s*=\s*([0-9]+)" [addr;value] -> vmem_mask_write (int64 addr) (int64 value) (mask |> Seq.toList)  0L
                                                                                   travel2 tail mask
                       | _ -> printfn "ERROR: non code %s" h
        | _  -> printfn "part2_%s: %A (3219837697833)" filespec (vmem.Values |> Seq.sum)


travel2 lines "0" //Part 2

// for i in vmem.Keys do
//    printfn "mem[%012X] = %9d" i vmem.[i]

(*
 "mask = 110X0010110X1X100010101X00100X001010"
"mem[30968] = 2095418"
"mem[3121] = 139148"
"mem[53666] = 26824"
part2_input.day14.txt: 3219837697833L
        0.99 real         0.22 user         0.02 sys

Compilation finished at Sun Dec 13 23:58:37

*)
