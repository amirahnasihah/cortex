# Astro - Deployment


## Deploy

# Deploy your Astro Site

 Ready to build and deploy your Astro site? Follow one of our guides to different deployment services or scroll down for general guidance about deploying an Astro site.

## Deployment Guides
 Section titled “Deployment Guides”

 -

###

 AWS

 On demand Static

-

###

 AWS via Flightcontrol

 On demand Static

-

###

 AWS via SST

 On demand Static

-

###

 Azion

 On demand Static

-

###

 Buddy

 Static

-

###

 Cleavr

 On demand Static

-

###

 Clever Cloud

 Static On demand

-

###

 Cloudflare

 On demand Static

-

###

 CloudRay

 Static

-

###

 Deno Deploy

 On demand Static

-

###

 DeployHQ

 Static

-

###

 EdgeOne Pages

 On demand Static

-

###

 Firebase

 On demand Static

-

###

 Fleek

 Static

-

###

 Fly.io

 On demand Static

-

###

 GitHub Pages

 Static

-

###

 GitLab Pages

 Static

-

###

 Google Cloud

 On demand Static

-

###

 Heroku

 Static

-

###

 Hostinger

 On demand Static

-

###

 Juno

 Static

-

###

 Microsoft Azure

 Static

-

###

 Netlify

 On demand Static

-

###

 Railway

 On demand Static

-

###

 Render

 Static

-

###

 Seenode

 On demand

-

###

 Sevalla

 On demand Static

-

###

 Stormkit

 Static

-

###

 Surge

 Static

-

###

 Vercel

 On demand Static

-

###

 Zeabur

 On demand Static

-

###

 Zephyr Cloud

 Static

-

###

 Zerops

 On demand Static

## Quick Deploy Options
 Section titled “Quick Deploy Options”
 You can build and deploy an Astro site to a number of hosts quickly using either their website’s dashboard UI or a CLI.

### Website UI
 Section titled “Website UI”
 A quick way to deploy your website is to connect your Astro project’s online Git repository (e.g. GitHub, GitLab, Bitbucket) to a host provider and take advantage of continuous deployment using Git.

These host platforms automatically detect pushes to your Astro project’s source repository, build your site and deploy it to the web at a custom URL or your personal domain. Often, setting up a deployment on these platforms will follow steps something like the following:

-
Add your repository to an online Git provider (e.g. in GitHub, GitLab, Bitbucket)

-
Choose a host that supports continuous deployment (e.g. Netlify or Vercel ) and import your Git repository as a new site/project.

Many common hosts will recognize your project as an Astro site, and should choose the appropriate configuration settings to build and deploy your site as shown below. (If not, these settings can be changed.)

-
Click “Deploy” and your new website will be created at a unique URL for that host (e.g. `new-astro-site.netlify.app`).

The host will be automatically configured to watch your Git provider’s main branch for changes, and to rebuild and republish your site at each new commit. These settings can typically be configured in your host provider’s dashboard UI.

### CLI Deployment
 Section titled “CLI Deployment”
 Some hosts will have their own command line interface (CLI) you can install globally to your machine using npm. Often, using a CLI to deploy looks something like the following:

-
Install your host’s CLI globally, for example:

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npm install --global netlify-cli `

 Terminal window
```
` pnpm add --global netlify-cli `
```

 Terminal window
```
` yarn global add netlify-cli `
```

-
 Run the CLI and follow any instructions for authorization, setup etc.

-
Build your site and deploy to your host

Many common hosts will build and deploy your site for you. They will usually recognize your project as an Astro site, and should choose the appropriate configuration settings to build and deploy as shown below. (If not, these settings can be changed.)

Other hosts will require you to build your site locally and deploy using the command line.

## Building Your Site Locally
 Section titled “Building Your Site Locally”
 Many hosts like Netlify and Vercel will build your site for you and then publish that build output to the web. But, some sites will require you to build locally and then run a deploy command or upload your build output.

You may also wish to build locally to preview your site, or to catch any potential errors and warnings in your own environment.

Run the command `npm run build` to build your Astro site.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run build `

 Terminal window
```
` pnpm run build `
```

 Terminal window
```
` yarn run build `
```

 By default, the build output will be placed at `dist/`. This location can be changed using the `outDir` configuration option .

## Adding an Adapter for on-demand rendering
 Section titled “Adding an Adapter for on-demand rendering”

 Recipes

 Contribute

 Community

 Sponsor

## Cloudflare

# Deploy your Astro Site to Cloudflare

 You can deploy full-stack applications, including front-end static assets and back-end APIs, as well as on-demand rendered sites, to Cloudflare Workers .

 Read more about using the Cloudflare runtime in your Astro project.

## Prerequisites
 Section titled “Prerequisites”
 To get started, you will need:

- A Cloudflare account. If you don’t already have one, you can create a free Cloudflare account during the process.

## Cloudflare Workers
 Section titled “Cloudflare Workers”

### How to deploy with Wrangler
 Section titled “How to deploy with Wrangler”

-
 Install Wrangler CLI .

 Terminal window ` npm install wrangler@latest --save-dev `

-
 If your site uses on-demand rendering, install the `@astrojs/cloudflare` adapter .

This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx astro add cloudflare `

 Terminal window
```
` pnpm astro add cloudflare `
```

 Terminal window
```
` yarn astro add cloudflare `
```

 Read more about on-demand rendering in Astro .

-
 Create a Wrangler configuration file .

Running `astro add cloudflare` will create this for you; if you are not using the adapter, you’ll need to create it yourself.

 Static

-

 On demand

 wrangler.jsonc ` { "name" : " my-astro-app " , "compatibility_date" : " YYYY-MM-DD " , // Update to the day you deploy "assets" : { "directory" : " ./dist " , } } `

 wrangler.jsonc
```
` { "main" : " dist/_worker.js/index.js " , "name" : " my-astro-app " , "compatibility_date" : " YYYY-MM-DD " , // Update to the day you deploy "compatibility_flags" : [ " nodejs_compat " , " global_fetch_strictly_public " ], "assets" : { "binding" : " ASSETS " , "directory" : " ./dist " }, "observability" : { "enabled" : true } } `
```

-
 Preview your project locally with Wrangler.

 Terminal window ` npx astro build &#x26;&#x26; npx wrangler dev `

-
 Deploy using `npx wrangler deploy`.

 Terminal window ` npx astro build &#x26;&#x26; npx wrangler deploy `

 After your assets are uploaded, Wrangler will give you a preview URL to inspect your site.

 Read more about using Cloudflare runtime APIs such as bindings.

### How to deploy with CI/CD
 Section titled “How to deploy with CI/CD”
 You can also use a CI/CD system such as Workers Builds to automatically build and deploy your site on push.

If you’re using Workers Builds:

-
Follow Steps 1-3 from the Wrangler section above.

-
Log in to the Cloudflare dashboard and navigate to `Compute > Workers &#x26; Pages`. Select `Create application`.

-
Under `Import a repository`, select a Git account and then the repository containing your Astro project.

-
Configure your project with:

 Build command: `npx astro build`

- Deploy command: `npx wrangler deploy`

-
Click `Save and Deploy`. You can now preview your Worker at its provided `workers.dev` subdomain.

## Troubleshooting
 Section titled “Troubleshooting”

### 404 behavior
 Section titled “404 behavior”
 For Workers projects, you will need to set `not_found_handling` if you want to serve a custom 404 page. You can read more about this in the Routing behavior section of Cloudflare’s documentation.

 wrangler.jsonc ` { "assets" : { "directory" : " ./dist " , "not_found_handling" : " 404-page " } } `

### Client-side hydration
 Section titled “Client-side hydration”
 Client-side hydration may fail as a result of Cloudflare’s Auto Minify setting. If you see `Hydration completed but contains mismatches` in the console, make sure to disable Auto Minify under Cloudflare settings.

### Node.js runtime APIs
 Section titled “Node.js runtime APIs”
 If you are building a project that is using on-demand rendering with the Cloudflare adapter and the server fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

-
This means that a package or import you are using in the server-side environment is not compatible with the Cloudflare runtime APIs .

-
If you are directly importing a Node.js runtime API, please refer to the Astro documentation on Cloudflare’s Node.js compatibility for further steps on how to resolve this.

-
If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Netlify

# Deploy your Astro Site to Netlify

 Netlify offers hosting and serverless backend services for web applications and static websites. Any Astro site can be hosted on Netlify!

This guide includes instructions for deploying to Netlify through the website UI or Netlify’s CLI.

## Project configuration
 Section titled “Project configuration”
 Your Astro project can be deployed to Netlify in three different ways: as a static site, a server-rendered site, or an edge-rendered site.

### Static site
 Section titled “Static site”
 Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Netlify.

### Adapter for on-demand rendering
 Section titled “Adapter for on-demand rendering”
 Add the Netlify adapter to enable on-demand rendering in your Astro project and deploy to Netlify with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

 - Terminal window ` npx astro add netlify `

 See the Netlify adapter guide to install manually instead, or for more configuration options, such as deploying your project’s Astro middleware using Netlify’s Edge Functions.

## How to deploy
 Section titled “How to deploy”
 You can deploy to Netlify through the website UI or using Netlify’s CLI (command line interface). The process is the same for both static and on-demand rendered Astro sites.

### Website UI deployment
 Section titled “Website UI deployment”
 If your project is stored in GitHub, GitLab, BitBucket, or Azure DevOps, you can use the Netlify website UI to deploy your Astro site.

Click Add a new site in your Netlify dashboard

-
Choose Import an existing project

When you import your Astro repository from your Git provider, Netlify should automatically detect and pre-fill the correct configuration settings for you.

-
Make sure that the following settings are entered, then press the Deploy button:

 Build Command: `astro build` or `npm run build`

- Publish directory: `dist`

After deploying, you will be redirected to the site overview page. There, you can edit the details of your site.

Any future changes to your source repository will trigger preview and production deploys based on your deployment configuration.

#### `netlify.toml` file
 Section titled “netlify.toml file”
 You can optionally create a new `netlify.toml` file at the top level of your project repository to configure your build command and publish directory, as well as other project settings including environment variables and redirects. Netlify will read this file and automatically configure your deployment.

To configure the default settings, create a `netlify.toml` file with the following contents:

 ` [build] command = " npm run build " publish = " dist " `

 More info at “Deploying an existing Astro Git repository” on Netlify’s blog

### CLI deployment
 Section titled “CLI deployment”
 You can also create a new site on Netlify and link up your Git repository by installing and using the Netlify CLI .

-
Install Netlify’s CLI globally

 Terminal window ` npm install --global netlify-cli `

-
 Run `netlify login` and follow the instructions to log in and authorize Netlify

-
Run `netlify init` and follow the instructions

-
Confirm your build command (`astro build`)

The CLI will automatically detect the build settings (`astro build`) and deploy directory (`dist`), and will offer to automatically generate a `netlify.toml` file with those settings.

-
Build and deploy by pushing to Git

The CLI will add a deploy key to the repository, which means your site will be automatically rebuilt on Netlify every time you `git push`.

 More details from Netlify on Deploy an Astro site using the Netlify CLI

### Set a Node.js version
 Section titled “Set a Node.js version”
 If you are using a legacy build image (Xenial) on Netlify, make sure that your Node.js version is set. Astro requires `v22.12.0` or higher.

You can specify your Node.js version in Netlify using:

- a `.nvmrc` file in your base directory.

- a `NODE_VERSION` environment variable in your site’s settings using the Netlify project dashboard.

## Using Netlify Functions
 Section titled “Using Netlify Functions”
 No special configuration is required to use Netlify Functions with Astro. Add a `netlify/functions` directory to your project root and follow the Netlify Functions documentation to get started!

## Examples
 Section titled “Examples”

- Deploy An Astro site with Forms, Serverless Functions, and Redirects — Netlify Blog

- Deployment Walkthrough Video — Netlify YouTube channel

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Vercel

# Deploy your Astro Site to Vercel

 You can use Vercel to deploy an Astro site to their global edge network with zero configuration.

This guide includes instructions for deploying to Vercel through the website UI or Vercel’s CLI.

## Project configuration
 Section titled “Project configuration”
 Your Astro project can be deployed to Vercel as a static site, or a server-rendered site.

### Static site
 Section titled “Static site”
 Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Vercel.

### Adapter for on-demand rendering
 Section titled “Adapter for on-demand rendering”
 Add the Vercel adapter to enable on-demand rendering in your Astro project with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add vercel `

 Terminal window
```
` pnpm astro add vercel `
```

 Terminal window
```
` yarn astro add vercel `
```

 See the Vercel adapter guide to install manually instead, or for more configuration options, such as deploying your project’s Astro middleware using Vercel Edge Functions.

## How to deploy
 Section titled “How to deploy”
 You can deploy to Vercel through the website UI or using Vercel’s CLI (command line interface). The process is the same for both static and on-demand rendered Astro sites.

### Website UI deployment
 Section titled “Website UI deployment”

 Push your code to your online Git repository (GitHub, GitLab, BitBucket).

-
 Import your project into Vercel.

-
Vercel will automatically detect Astro and configure the right settings.

-
Your application is deployed! (e.g. astro.vercel.app )

After your project has been imported and deployed, all subsequent pushes to branches will generate Preview Deployments , and all changes made to the Production Branch (commonly “main”) will result in a Production Deployment .

 Learn more about Vercel’s Git Integration .

### CLI deployment
 Section titled “CLI deployment”

-
 Install the Vercel CLI and run `vercel` to deploy.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install -g vercel vercel `

 Terminal window
```
` pnpm add -g vercel vercel `
```

 Terminal window
```
` yarn global add vercel vercel `
```

-
 Vercel will automatically detect Astro and configure the right settings.

-
When asked `Want to override the settings? [y/N]`, choose `N`.

-
Your application is deployed! (e.g. astro.vercel.app )

### Project config with `vercel.json`
 Section titled “Project config with vercel.json”
 You can use `vercel.json` to override the default behavior of Vercel and to configure additional settings. For example, you may wish to attach headers to HTTP responses from your Deployments.

 Learn more about Vercel’s project configuration .

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Github

# Deploy your Astro Site to GitHub Pages

 You can use GitHub Pages to host a static, prerendered Astro website directly from a repository on GitHub.com using GitHub Actions .

## How to deploy
 Section titled “How to deploy”
 Astro maintains an official Astro GitHub Action to deploy your project to a GitHub Pages with very little configuration and is the recommended way to deploy to GitHub Pages.

Follow the instructions below to use the GitHub Action to deploy your Astro site to GitHub Pages. This will create a website from your repository at a GitHub URL (e.g. `https://&#x3C;username>.github.io/&#x3C;my-repo>`). Once deployed, you can optionally configure a custom domain to deploy your GitHub Pages site at your preferred domain (e.g. `https://example.com`).

-
Create a new file in your project at `.github/workflows/deploy.yml` and paste in the YAML below.

 deploy.yml ` name : Deploy to GitHub Pages
 on : # Trigger the workflow every time you push to the `main` branch # Using a different branch name? Replace `main` with your branch’s name push : branches : [ main ] # Allows you to run this workflow manually from the Actions tab on GitHub. workflow_dispatch :
 # Allow this job to clone the repo and create a page deployment permissions : contents : read pages : write id-token : write
 jobs : build : runs-on : ubuntu-latest steps : - name : Checkout your repository using git uses : actions/checkout@v6 - name : Install, build, and upload your site uses : withastro/action@v6 # with: # path: . # The root location of your Astro project inside the repository. (optional) # node-version: 24 # The specific version of Node that should be used to build your site. Defaults to 24. (optional) # package-manager: pnpm@latest # The Node package manager that should be used to install dependencies and build your site. Automatically detected based on your lockfile. (optional) # build-cmd: pnpm run build # The command to run to build your site. Runs the package build script/task by default. (optional) # env: # PUBLIC_POKEAPI: 'https://pokeapi.co/api/v2' # Use single quotation marks for the variable value. (optional)
 deploy : needs : build runs-on : ubuntu-latest environment : name : github-pages url : ${{ steps.deployment.outputs.page_url }} steps : - name : Deploy to GitHub Pages id : deployment uses : actions/deploy-pages@v5 `
 The Astro action can be configured with optional inputs. Provide these by uncommenting the `with:` line and the input you want to use.

If your site requires any public environment variables, uncomment the `env:` line and add them there. (See the GitHub documentation on setting secrets for adding private environment variables.)

-
In your Astro config file, set `site` to the GitHub URL of your deployed site.

 astro.config.mjs ` import { defineConfig } from ' astro/config '
 export default defineConfig ({ site: ' https://astronaut.github.io ' , }) `
 The value for `site` must be one of the following:

 The following URL based on your username: `https://&#x3C;username>.github.io`

- The random URL autogenerated for a GitHub Organization’s private page : `https://&#x3C;random-string>.pages.github.io/`

-
In `astro.config.mjs`, configure a value for `base` (usually required).

GitHub Pages will publish your website at an address that depends on both your username and your repository name (e.g. `https://&#x3C;username>.github.io/&#x3C;my-repo>/`). Set a value for `base` that specifies the repository for your website. This is so that Astro understands your website’s root is `/my-repo`, rather than the default `/`. You can skip this if your repository name matches the special `&#x3C;username>.github.io` pattern (e.g. `https://github.com/username/username.github.io/`)

Configure `base` as the repository’s name starting with a forward slash ( e.g. `/my-repo`):

 astro.config.mjs ` import { defineConfig } from ' astro/config '
 export default defineConfig ({ site: ' https://astronaut.github.io ' , base: ' /my-repo ' , }) `

-
 On GitHub, go to your repository’s Settings tab and find the Pages section of the settings.

-
Choose GitHub Actions as the Source of your site.

When you push changes to your Astro project’s repository, the GitHub Action will automatically deploy them for you at your GitHub URL.

## Change your GitHub URL to a custom domain
 Section titled “Change your GitHub URL to a custom domain”
 Once your Astro project is deployed to GitHub pages at a GitHub URL following the previous instructions, you can configure a custom domain. This means that users can visit your site at your custom domain `https://example.com` instead of `https://&#x3C;username>.github.io`.

-
 Configure DNS for your domain provider .

-
Add a `./public/CNAME` record to your project.

Create the following file in your `public/` folder with a single line of text that specifies your custom domain:

 public/CNAME ` sub . example . com `
 This will deploy your site at your custom domain instead of `user.github.io`.

-
In your Astro config, update the value for `site` with your custom domain. Do not set a value for `base`, and remove one if it exists:

 astro.config.mjs ` import { defineConfig } from ' astro/config '
 export default defineConfig ({ site: ' https://example.com ' , base: ' /my-repo ' }) `

-
 If necessary, update all your page internal links to remove the `base` prefix:

```
` &#x3C; a href = " /my-repo /about " > About &#x3C;/ a > `
```
 About ">

## Examples
 Section titled “Examples”

- Github Pages Deployment starter template

- Starlight Flexoki Theme (production site)

- Expressive Code Color Chips (production site)

- Starlight Markdown Blocks (production site)

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Aws

# Deploy your Astro Site to AWS

 AWS is a full-featured web app hosting platform that can be used to deploy an Astro site.

Deploying your project to AWS requires using the AWS console . (Most of these actions can also be done using the AWS CLI ). This guide will walk you through the steps to deploy your site to AWS using AWS Amplify , S3 static website hosting , and CloudFront .

## AWS Amplify
 Section titled “AWS Amplify”
 AWS Amplify is a set of purpose-built tools and features that lets frontend web and mobile developers quickly and easily build full-stack applications on AWS. You can either deploy your Astro project as a static site, or as a server-rendered site.

### Static Site
 Section titled “Static Site”
 Your Astro project is a static site by default.

-
Create a new Amplify Hosting project.

-
Connect your repository to Amplify.

-
Modify your build settings to match your project’s build process.

 npm

-

 pnpm

-

 Yarn

 ` version : 1 frontend : phases : preBuild : commands : - npm ci build : commands : - npm run build artifacts : baseDirectory : /dist files : - ' **/* ' cache : paths : - node_modules/**/* `

 -
```
` version : 1 frontend : phases : preBuild : commands : - npm i -g pnpm - pnpm config set store-dir .pnpm-store - pnpm i build : commands : - pnpm run build artifacts : baseDirectory : /dist files : - ' **/* ' cache : paths : - .pnpm-store/**/* `
```

```
` version : 1 frontend : phases : preBuild : commands : - yarn install build : commands : - yarn build artifacts : baseDirectory : /dist files : - ' **/* ' cache : paths : - node_modules/**/* `
```

 Amplify will automatically deploy your website and update it when you push a commit to your repository.

### Adapter for on-demand rendering
 Section titled “Adapter for on-demand rendering”
 In order to deploy your project as a server-rendered site, you will need to use the third-party, community-maintained AWS Amplify adapter and make some changes to your config.

First, install the Amplify adapter.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install astro-aws-amplify `

 Terminal window
```
` pnpm add astro-aws-amplify `
```

 Terminal window
```
` yarn add astro-aws-amplify `
```

 Then, in your `astro.config.*` file, add the adapter and set the output to `server`.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import awsAmplify from ' astro-aws-amplify ' ;
 export default defineConfig ({ // ... output: " server " , adapter: awsAmplify (), }); `
 Once the adapter has been installed, you can set up your Amplify project.

-
Create a new Amplify Hosting project.

-
Connect your repository to Amplify.

-
Modify your build settings to match the adapter’s build process by either editing the build settings in the AWS console, or by adding an `amplify.yaml` in the root of your project.

 npm

-

 pnpm

-

 Yarn

 ` version : 1 frontend : phases : preBuild : commands : - npm ci --cache .npm --prefer-offline build : commands : - npm run build - mv node_modules ./.amplify-hosting/compute/default artifacts : baseDirectory : .amplify-hosting files : - ' **/* ' cache : paths : - .npm/**/* `

```
` version : 1 frontend : phases : preBuild : commands : - npm i -g pnpm - pnpm config set store-dir .pnpm-store - pnpm i build : commands : - pnpm run build - mv node_modules ./.amplify-hosting/compute/default artifacts : baseDirectory : .amplify-hosting files : - ' **/* ' cache : paths : - .pnpm-store/**/* `
```

```
` version : 1 frontend : phases : preBuild : commands : - yarn install build : commands : - yarn build - mv node_modules ./.amplify-hosting/compute/default artifacts : baseDirectory : .amplify-hosting files : - ' **/* ' cache : paths : - node_modules/**/* `
```

 Amplify will automatically deploy your website and update it when you push a commit to your repository.

 See AWS’s Astro deployment guide for more info.

## S3 static website hosting
 Section titled “S3 static website hosting”
 S3 is the starting point of any application. It is where your project files and other assets are stored. S3 charges for file storage and number of requests. You can find more information about S3 in the AWS documentation .

-
Create an S3 bucket with your project’s name.

-
Disable “Block all public access” . By default, AWS sets all buckets to be private. To make it public, you need to uncheck the “Block public access” checkbox in the bucket’s properties.

-
Upload your built files located in `dist` to S3. You can do this manually in the console or use the AWS CLI. If you use the AWS CLI, use the following command after authenticating with your AWS credentials :

 ` aws s3 cp dist/ s3://&#x3C;BUCKET_NAME>/ --recursive ` / --recursive">

-
 Update your bucket policy to allow public access. You can find this setting in the bucket’s Permissions > Bucket policy .

 ` { "Version" : " 2012-10-17 " , "Statement" : [ { "Sid" : " PublicReadGetObject " , "Effect" : " Allow " , "Principal" : " * " , "Action" : " s3:GetObject " , "Resource" : " arn:aws:s3:::&#x3C;BUCKET_NAME>/* " } ] } ` /*&#x22; } ]}">

-
 Enable website hosting for your bucket. You can find this setting in the bucket’s Properties > Static website hosting . Set your index document to `index.html` and your error document to `404.html`. Finally, you can find your new website URL in the bucket’s Properties > Static website hosting .

## S3 with CloudFront
 Section titled “S3 with CloudFront”
 CloudFront is a web service that provides content delivery network (CDN) capabilities. It is used to cache content of a web server and distribute it to end users. CloudFront charges for the amount of data transferred. Adding CloudFront to your S3 bucket is more cost-effective and provides a faster delivery.

To connect S3 with CloudFront, create a CloudFront distribution with the following values:

- Origin domain: Your S3 bucket static website endpoint. You can find your endpoint in your S3 bucket’s Properties > Static website hosting . Alternative, you can select your s3 bucket and click on the callout to replace your bucket address with your bucket static endpoint.

- Viewer protocol policy: “Redirect to HTTPS”

This configuration will serve your site using the CloudFront CDN network. You can find your CloudFront distribution URL in the bucket’s Distributions > Domain name .

## Continuous deployment with GitHub Actions
 Section titled “Continuous deployment with GitHub Actions”
 There are many ways to set up continuous deployment for AWS. One possibility for code hosted on GitHub is to use GitHub Actions to deploy your website every time you push a commit.

-
Create a new policy in your AWS account using IAM with the following permissions. This policy will allow you to upload built files to your S3 bucket and invalidate the CloudFront distribution files when you push a commit.

 ` { "Version" : " 2012-10-17 " , "Statement" : [ { "Sid" : " VisualEditor0 " , "Effect" : " Allow " , "Action" : [ " s3:PutObject " , " s3:ListBucket " , " s3:DeleteObject " , " cloudfront:CreateInvalidation " ], "Resource" : [ " &#x3C;DISTRIBUTION_ARN> " , " arn:aws:s3:::&#x3C;BUCKET_NAME>/* " , " arn:aws:s3:::&#x3C;BUCKET_NAME> " ] } ] } ` &#x22;, &#x22;arn:aws:s3::: /*&#x22;, &#x22;arn:aws:s3::: &#x22; ] } ]}">

-
 Create a new IAM user and attach the policy to the user. This will provide your `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID`.

-
Add this sample workflow to your repository at `.github/workflows/deploy.yml` and push it to GitHub. You will need to add `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `BUCKET_ID`, and `DISTRIBUTION_ID` as “secrets” to your repository on GitHub under Settings > Secrets > Actions . Click New repository secret to add each one.

```
` name : Deploy Website
 on : push : branches : - main
 jobs : deploy : runs-on : ubuntu-latest steps : - name : Checkout uses : actions/checkout@v6 - name : Configure AWS Credentials uses : aws-actions/configure-aws-credentials@v1 with : aws-access-key-id : ${{ secrets.AWS_ACCESS_KEY_ID }} aws-secret-access-key : ${{ secrets.AWS_SECRET_ACCESS_KEY }} aws-region : us-east-1 - name : Install modules run : npm ci - name : Build application run : npm run build - name : Deploy to S3 run : aws s3 sync --delete ./dist/ s3://${{ secrets.BUCKET_ID }} - name : Create CloudFront invalidation run : aws cloudfront create-invalidation --distribution-id ${{ secrets.DISTRIBUTION_ID }} --paths "/*" `
```

## Community Resources
 Section titled “Community Resources”

- Deploy Astro to AWS Amplify

- Deploy Astro to AWS Elastic Beanstalk

- Deploy Astro to Amazon ECS on AWS Fargate

- Troubleshooting SSR Amplify Deployments

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Flyio

# Deploy your Astro Site to Fly.io

 You can deploy your Astro project to Fly.io , a platform for running full stack apps and databases close to your users.

## Project Configuration
 Section titled “Project Configuration”
 Your Astro project can be deployed to Fly.io as a static site, or as a server-side rendered site (SSR).

### Static Site
 Section titled “Static Site”
 Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Fly.io.

### Adapter for SSR
 Section titled “Adapter for SSR”
 To enable on-demand rendering in your Astro project and deploy on Fly.io, add the Node.js adapter .

## How to deploy
 Section titled “How to deploy”

-
 Sign up for Fly.io if you haven’t already.

-
 Install `flyctl` , your Fly.io app command center.

-
Run the following command in your terminal.

 Terminal window ` fly launch `
 `flyctl` will automatically detect Astro, configure the correct settings, build your image, and deploy it to the Fly.io platform.

## Generating your Astro Dockerfile
 Section titled “Generating your Astro Dockerfile”
 If you don’t already have a Dockerfile, `fly launch` will generate one for you, as well as prepare a `fly.toml` file. For pages rendered on demand, this Dockerfile will include the appropriate start command and environment variables.

You can instead create your own Dockerfile using Dockerfile generator and then run using the command `npx dockerfile` for Node applications or `bunx dockerfile` for Bun applications.

## Official Resources
 Section titled “Official Resources”

- Check out the official Fly.io docs

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Deno

# Deploy your Astro Site with Deno

 You can deploy a static or on-demand rendered Astro site using Deno, either on your own server, or to Deno Deploy , a distributed system that runs JavaScript, TypeScript, and WebAssembly at the edge, worldwide.

This guide includes instructions for running your Astro site on your own server with Deno, and deploying to Deno Deploy through GitHub Actions or the Deno Deploy CLI.

## Requirements
 Section titled “Requirements”
 This guide assumes you already have Deno installed.

## Project Configuration
 Section titled “Project Configuration”
 Your Astro project can be deployed as a static site, or as an on-demand rendered site.

### Static Site
 Section titled “Static Site”
 Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site with Deno, or to Deno Deploy.

### Adapter for on-demand rendering
 Section titled “Adapter for on-demand rendering”
 To enable on-demand rendering in your Astro project using Deno, and to deploy on Deno Deploy:

-
Install the `@deno/astro-adapter` adapter to your project’s dependencies using your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npm install @deno/astro-adapter `

 Terminal window
```
` pnpm install @deno/astro-adapter `
```

 Terminal window
```
` yarn add @deno/astro-adapter `
```

-
 Update your `astro.config.mjs` project configuration file with the changes below.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import deno from ' @deno/astro-adapter ' ;
 export default defineConfig ({ output: ' server ' , adapter: deno (), }); `

-
 Update your `preview` script in `package.json` with the change below.

 package.json ` { // ... "scripts" : { "dev" : " astro dev " , "start" : " astro dev " , "build" : " astro build " , "preview" : " astro preview " " preview " : " deno run --allow-net --allow-read --allow-env ./dist/server/entry.mjs " } } `
 You can now use this command to preview your production Astro site locally with Deno.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run preview `

 Terminal window
```
` pnpm run preview `
```

 Terminal window
```
` yarn run preview `
```

## How to deploy
 Section titled “How to deploy”
 You can run your Astro site on your own server, or deploy to Deno Deploy through GitHub Actions or using Deno Deploy’s CLI (command line interface).

### On your own server
 Section titled “On your own server”

-
 Copy your project onto your server.

-
Install the project dependencies using your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install `

 Terminal window
```
` pnpm install `
```

 Terminal window
```
` yarn `
```

-
 Build your Astro site with your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run build `

 Terminal window
```
` pnpm run build `
```

 Terminal window
```
` yarn run build `
```

-
 Start your application with the following command:

 Static

-

 On demand

 Terminal window ` deno run -A jsr:@std/http/file-server dist `

 Terminal window
```
` deno run -A ./dist/server/entry.mjs `
```

### GitHub Actions Deployment
 Section titled “GitHub Actions Deployment”
 If your project is stored on GitHub, the Deno Deploy website will guide you through setting up GitHub Actions to deploy your Astro site.

-
Push your code to a public or private GitHub repository.

-
Sign in on Deno Deploy with your GitHub account, and click on New Project .

-
Select your repository, the branch you want to deploy from, and select GitHub Action mode. (Your Astro site requires a build step, and cannot use Automatic mode.)

-
In your Astro project, create a new file at `.github/workflows/deploy.yml` and paste in the YAML below. This is similar to the YAML given by Deno Deploy, with the additional steps needed for your Astro site.

 Static

-

 On demand

 .github/workflows/deploy.yml ` name : Deploy on : [ push ]
 jobs : deploy : name : Deploy runs-on : ubuntu-latest permissions : id-token : write # Needed for auth with Deno Deploy contents : read # Needed to clone the repository
 steps : - name : Clone repository uses : actions/checkout@v6
 # Not using npm? Change `npm ci` to `yarn install` or `pnpm i` - name : Install dependencies run : npm ci
 # Not using npm? Change `npm run build` to `yarn build` or `pnpm run build` - name : Build Astro run : npm run build
 - name : Upload to Deno Deploy uses : denoland/deployctl@v1 with : project : my-deno-project # TODO: replace with Deno Deploy project name entrypoint : jsr:@std/http/file-server root : dist `

 .github/workflows/deploy.yml
```
` name : Deploy on : [ push ]
 jobs : deploy : name : Deploy runs-on : ubuntu-latest permissions : id-token : write # Needed for auth with Deno Deploy contents : read # Needed to clone the repository
 steps : - name : Clone repository uses : actions/checkout@v6
 # Not using npm? Change `npm ci` to `yarn install` or `pnpm i` - name : Install dependencies run : npm ci
 # Not using npm? Change `npm run build` to `yarn build` or `pnpm run build` - name : Build Astro run : npm run build
 - name : Upload to Deno Deploy uses : denoland/deployctl@v1 with : project : my-deno-project # TODO: replace with Deno Deploy project name entrypoint : dist/server/entry.mjs `
```

-
 After committing this YAML file, and pushing to GitHub on your configured deploy branch, the deploy should begin automatically!

You can track the progress using the “Actions” tab on your GitHub repository page, or on Deno Deploy .

### CLI Deployment
 Section titled “CLI Deployment”

-
 Install the Deno Deploy CLI .

 Terminal window ` deno install -gArf jsr:@deno/deployctl `

-
 Build your Astro site with your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run build `

 Terminal window
```
` pnpm run build `
```

 Terminal window
```
` yarn run build `
```

-
 Run `deployctl` to deploy!

 Static

-

 On demand

 Terminal window ` cd dist &#x26;&#x26; deployctl deploy jsr:@std/http/file-server `

 Terminal window
```
` deployctl deploy ./dist/server/entry.mjs `
```

 You can track all your deploys on Deno Deploy .

-
(Optional) To simplify the build and deploy into one command, add a `deploy-deno` script in `package.json`.

 Static

-

 On demand

 package.json ` { // ... "scripts" : { "dev" : " astro dev " , "start" : " astro dev " , "build" : " astro build " , "preview" : " astro preview " , "deno-deploy" : " npm run build &#x26;&#x26; cd dist &#x26;&#x26; deployctl deploy jsr:@std/http/file-server " } } `

 package.json
```
` { // ... "scripts" : { "dev" : " astro dev " , "start" : " astro dev " , "build" : " astro build " , "preview" : " deno run --allow-net --allow-read --allow-env ./dist/server/entry.mjs " , "deno-deploy" : " npm run build &#x26;&#x26; deployctl deploy ./dist/server/entry.mjs " } } `
```

 Then you can use this command to build and deploy your Astro site in one step.

 Terminal window
```
` npm run deno-deploy `
```

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor

## Firebase

# Deploy your Astro Site to Google’s Firebase Hosting

 Firebase Hosting is a service provided by Google’s Firebase app development platform, which can be used to deploy an Astro site.

See our separate guide for adding Firebase backend services such as databases, authentication, and storage.

## Project Configuration
 Section titled “Project Configuration”
 Your Astro project can be deployed to Firebase as a static site, or as a server-side rendered site (SSR).

### Static Site
 Section titled “Static Site”
 Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Firebase.

### Adapter for SSR
 Section titled “Adapter for SSR”
 To enable SSR in your Astro project and deploy on Firebase add the Node.js adapter .

## How to deploy
 Section titled “How to deploy”

-
 Install the Firebase CLI . This is a command-line tool that allows you to interact with Firebase from the terminal.

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npm install firebase-tools `

 Terminal window
```
` pnpm add firebase-tools `
```

 Terminal window
```
` yarn add firebase-tools `
```

-
 Authenticate the Firebase CLI with your Google account. This will open a browser window where you can log in to your Google account.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx firebase login `

 Terminal window
```
` pnpm exec firebase login `
```

 Terminal window
```
` yarn firebase login `
```

-
 Enable experimental web frameworks support. This is an experimental feature that allows the Firebase CLI to detect and configure your deployment settings for Astro.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx firebase experiments:enable webframeworks `

 Terminal window
```
` pnpm exec firebase experiments:enable webframeworks `
```

 Terminal window
```
` yarn firebase experiments:enable webframeworks `
```

-
 Initialize Firebase Hosting in your project. This will create a `firebase.json` and `.firebaserc` file in your project root.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx firebase init hosting `

 Terminal window
```
` pnpm exec firebase init hosting `
```

 Terminal window
```
` yarn firebase init hosting `
```

-
 Deploy your site to Firebase Hosting. This will build your Astro site and deploy it to Firebase.

 npm

-

 pnpm

-

 Yarn

 Terminal window
```
` npx firebase deploy --only hosting `
```

 Terminal window
```
` pnpm exec firebase deploy --only hosting `
```

 Terminal window
```
` yarn firebase deploy --only hosting `
```

## More Deployment Guides

 -

###

 AWS

-

###

 AWS via Flightcontrol

-

###

 AWS via SST

-

###

 Azion

-

###

 Buddy

-

###

 Cleavr

-

###

 Clever Cloud

-

###

 Cloudflare

-

###

 CloudRay

-

###

 Deno Deploy

-

###

 DeployHQ

-

###

 EdgeOne Pages

-

###

 Firebase

-

###

 Fleek

-

###

 Fly.io

-

###

 GitHub Pages

-

###

 GitLab Pages

-

###

 Google Cloud

-

###

 Heroku

-

###

 Hostinger

-

###

 Juno

-

###

 Microsoft Azure

-

###

 Netlify

-

###

 Railway

-

###

 Render

-

###

 Seenode

-

###

 Sevalla

-

###

 Stormkit

-

###

 Surge

-

###

 Vercel

-

###

 Zeabur

-

###

 Zephyr Cloud

-

###

 Zerops

 Recipes

 Contribute

 Community

 Sponsor