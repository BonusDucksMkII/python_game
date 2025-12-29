mosaic = """
#version 330
in vec2 in_vert;
void main()
{
    gl_Position = vec4(in_vert, 0., 1.);
}
output_color(H,V) = input_color(floor(H/size)*size, floor(V/size)*size)
"""