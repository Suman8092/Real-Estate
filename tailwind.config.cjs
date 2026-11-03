const palette = require('./brand-palette.json');
const white = '#FFFFFF', black = '#000000';
const neutrals = {50:white,100:white,200:white,300:palette.charcoal.hex,400:palette.charcoal.hex,500:palette.charcoal.hex,600:palette.charcoal.hex,700:black,800:black,900:black,950:black};
const gold = Object.fromEntries(Object.keys(neutrals).map(shade => [shade,palette.gold.hex]));
module.exports = {
  content: ['./*.html', './js/*.js'],
  theme: {
    colors: {inherit:'inherit',current:'currentColor',transparent:'transparent',black,white,gray:neutrals,blue:neutrals,yellow:gold,red:gold,emerald:gold,brand:{navy:black,blue:black,yellow:palette.gold.hex,yellowHover:palette.highlight.hex}},
    boxShadow: {sm:'none',DEFAULT:'none',md:'none',lg:'none',xl:'none','2xl':'none',inner:'none',none:'none'},
    extend: {fontFamily:{sans:['Poppins','sans-serif']},ringColor:{DEFAULT:palette.gold.hex},ringOpacity:{DEFAULT:'1'}}
  },
  plugins: []
};
