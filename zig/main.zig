const std = @import("std");
const print = std.debug.print;
pub fn main() void {
    var a = [3]i32{ 1, 3, 5 };
    for (a) |elem, i| {
        print("elem {}: {}\n", .{ i, elem });
    }
}
