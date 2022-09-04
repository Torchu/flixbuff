module.exports = {
  env: {
    browser: true,
    node: true
  },
  extends: [
    'plugin:@typescript-eslint/recommended',
    'plugin:@angular-eslint/recommended',
    'plugin:@angular-eslint/template/process-inline-templates'
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: 'tsconfig.eslint.json',
    tsconfigRootDir: __dirname,
    extraFileExtensions: '.html'
  },
  plugins: ['@typescript-eslint'],
  rules: {},
  overrides: [
    {
      files: '*.ts',
      rules: {
        curly: ['error', 'all'],
        'comma-dangle': ['error', 'never'],
        'lines-between-class-members': 'off',
        'max-len': ['error', { code: 120, ignorePattern: '^import .*' }],
        'no-restricted-imports': ['error', { paths: ['rxjs/Rx'] }],
        quotes: ['error', 'single', { allowTemplateLiterals: true }],
        'sort-imports': 'error',
        '@typescript-eslint/camelcase': 'off',
        '@typescript-eslint/explicit-function-return-type': [
          'error',
          { allowExpressions: true }
        ],
        '@typescript-eslint/explicit-member-accessibility': 'off',
        '@typescript-eslint/no-explicit-any': 'off',
        '@typescript-eslint/explicit-module-boundary-types': 'error',
        '@typescript-eslint/no-parameter-properties': 'off',
        '@typescript-eslint/no-unused-vars': [
          'warn',
          { argsIgnorePattern: '^_', varsIgnorePattern: '^ignored?$' }
        ],
        '@typescript-eslint/naming-convention': [
          'error',
          {
            selector: 'default',
            format: ['camelCase']
          },
          {
            selector: 'memberLike',
            modifiers: ['private'],
            format: ['camelCase'],
            leadingUnderscore: 'allow'
          },
          {
            selector: 'memberLike',
            format: ['camelCase'],
            leadingUnderscore: 'allow'
          },
          {
            selector: 'parameter',
            format: ['camelCase'],
            leadingUnderscore: 'allow'
          },
          {
            selector: 'variable',
            format: ['camelCase', 'UPPER_CASE']
          },
          {
            selector: 'typeLike',
            format: ['PascalCase']
          },
          {
            selector: 'enumMember',
            format: ['PascalCase']
          }
        ],
        '@angular-eslint/directive-selector': [
          'error',
          {
            type: 'attribute',
            prefix: 'app',
            style: 'camelCase'
          }
        ],
        '@angular-eslint/component-selector': [
          'error',
          {
            type: 'element',
            prefix: 'app',
            style: 'kebab-case'
          }
        ],
        indent: ['error', 2, { SwitchCase: 1 }]
      }
    },
    {
      files: '*.js',
      rules: {
        '@typescript-eslint/no-var-requires': 'off',
        'comma-dangle': ['error', 'never'],
        quotes: ['error', 'single', { allowTemplateLiterals: true }]
      }
    },
    {
      files: '*.spec.ts',
      rules: {
        '@typescript-eslint/no-use-before-define': 'off',
        '@typescript-eslint/no-unused-vars': 'off',
        '@typescript-eslint/explicit-function-return-type': 'off',
        'sort-imports': 'off',
        'comma-dangle': ['error', 'never'],
        quotes: ['error', 'single', { allowTemplateLiterals: true }]
      }
    },
    {
      files: '*.html',
      extends: 'plugin:@angular-eslint/template/recommended',
      rules: {
        'max-len': 'off',
        indent: 'off'
      }
    }
  ]
};
