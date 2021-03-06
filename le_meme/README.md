# Le Meme

A tool for making dank memes!

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'le_meme'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install le_meme

If you're getting extconf errors or something like that, make sure you have ImageMagick installed.

## Usage

### I WANT A MEME NOW!
Use the command-line tool, `meme`:

```sh
meme 'i want a' 'dank meme'
```
![](https://cloud.githubusercontent.com/assets/168193/5734047/7304be40-9b62-11e4-9b2b-0ccbadbb3aa1.jpg)

### I want to see the command line options
You can do most meme-ish things from the command-line. It has interactive help at `meme -h`.  
Should be straightforward enough for even the dankest memer.

### I want to make memes in my ruby application
Easy enough!

#### Using a template
```ruby
require 'le_meme'
LeMeme::MemeLib.new_with_default_memes.meme(template: 'maymay', top: 'Top text', bottom: 'Bottom Text').to_file
```

#### Using any old image

```ruby
require 'le_meme'
LeMeme::Meme.new('~/Desktop/to_be_memed.jpg', top: 'Top text', bottom: 'bottom text').to_file
```

See the [docs](http://www.rubydoc.info/gems/le_meme) for all the memetastic details

## Contributing

1. Fork it ( https://github.com/paradox460/le_meme/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## WHY?
Because the world needs more dank memes!

Actually, because I wanted to take some time and clean up the core of [memebot](http://github.com/paradox460/memebot), and figured making the essential meme generation a gem was the best way to do it. Now I can spam my coworkers with memes in hipchat as well.

## LICENSE
```
Copyright (c) 2015 Jeff Sandberg

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
