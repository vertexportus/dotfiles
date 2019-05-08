mkdir Github
cd Github

# Material Design Icons
git clone --depth 1 https://github.com/google/material-design-icons
ln -s $PWD/material-design-icons/iconfont/MaterialIcons-Regular.ttf ~/.fonts/

# Community Fork
git clone --depth 1 https://github.com/Templarian/MaterialDesign-Webfont
ln -s $PWD/MaterialDesign-Webfont/fonts/materialdesignicons-webfont.ttf ~/.fonts/

# FontAwesome
git clone --depth 1 https://github.com/FortAwesome/Font-Awesome
ln -s "$PWD/Font-Awesome/otfs/Font Awesome 5 Free-Solid-900.otf" ~/.fonts/
ln -s "$PWD/Font-Awesome/otfs/Font Awesome 5 Free-Regular-400.otf" ~/.fonts/
ln -s "$PWD/Font-Awesome/otfs/Font Awesome 5 Brands-Regular-400.otf" ~/.fonts/

# Ionicons
git clone --depth 1 https://github.com/ionic-team/ionicons
ln -s $PWD/ionicons/docs/fonts/ionicons.ttf ~/.fonts/

# Typicons
git clone --depth 1 https://github.com/stephenhutchings/typicons.font
ln -s $PWD/typicons.font/src/font/typicons.ttf ~/.fonts/
